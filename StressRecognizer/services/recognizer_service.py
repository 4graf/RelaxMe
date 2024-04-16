import mne
import numpy as np
from numpy import ndarray
from scipy.stats import skew, kurtosis

from StressRecognizer.constants import DefaultSettings
from StressRecognizer.interfaces.services.abstract_recognizer_service import AbstractRecognizerService


class RecognizerService(AbstractRecognizerService):

    async def extract_features(self, data: ndarray):
        feat_data = self._bci_data_to_mne(data)
        feat_data = self._filter_eeg(feat_data)
        feat_data = self._extract_features(feat_data)

        return feat_data

    async def predict_stress(self, data: ndarray):
        ...

    def _bci_data_to_mne(data, ch_names=DefaultSettings.eeg_channel_names, sfreq=DefaultSettings.sfreq):
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=['eeg'] * len(ch_names), verbose=False)
        eeg = mne.io.RawArray(data=data, info=info, verbose=False)
        eeg = eeg.set_eeg_reference(verbose=False)
        return eeg

    def _filter_eeg(data, low_cutoff=DefaultSettings.low_cutoff, high_cutoff=DefaultSettings.high_cutoff):
        data_filt = data.copy()

        data_notched = mne.filter.notch_filter(
            data_filt.get_data(),
            Fs=data_filt.info["sfreq"],
            freqs=50,
            verbose=False
        )
        data_filt = mne.io.RawArray(data=data_notched, info=data_filt.info, verbose=False)

        data_filt.filter(l_freq=low_cutoff, h_freq=high_cutoff, method='iir', verbose=False)
        return data_filt

    def _extract_features(data, epoch_duration=DefaultSettings.epoch_duration):
        eeg_epochs = mne.make_fixed_length_epochs(data, epoch_duration, verbose=False)

        psd_alpha = eeg_epochs.compute_psd(fmin=8, fmax=13, verbose=False)
        psd_beta = eeg_epochs.compute_psd(fmin=13, fmax=40, verbose=False)
        psd_alpha = psd_alpha.get_data()
        psd_beta = psd_beta.get_data()
        features = np.hstack((psd_alpha.reshape((psd_alpha.shape[0], -1)),
                              psd_beta.reshape((psd_beta.shape[0], -1))))

        # mean_powers = []
        for psd in (psd_alpha, psd_beta):
            mean_power = np.mean(psd, axis=2)
            # mean_powers.append(mean_power)
            median_power = np.median(psd, axis=2)
            std_power = np.std(psd, axis=2)
            # var_power = np.var(psd, axis=1)
            skewness_power = skew(psd, axis=2)
            kurtosis_power = kurtosis(psd, axis=2)

            features = np.hstack((features, mean_power, median_power, std_power, skewness_power, kurtosis_power))
            # names.append()

        # mean_powers = [a/b for a, b in ]
        # features = np.hstack((features, mean_powers))
        return features
