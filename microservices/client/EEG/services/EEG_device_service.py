from brainflow import BrainFlowInputParams, BoardShim, BoardIds


class EEGDeviceService:

    def __init__(self, board_ids=BoardIds.CYTON_BOARD, serial_port='COM3'):
        params = BrainFlowInputParams()
        params.serial_port = serial_port

        self.board = BoardShim(BoardIds.SYNTHETIC_BOARD, params)
        # self.board = BoardShim(board_ids, params)
        self.board.prepare_session()

        self.sampling_rate = self.board.get_sampling_rate(board_ids)
        self.channel_names = self.board.get_eeg_names(board_ids)
        self.eeg_channels = BoardShim.get_eeg_channels(board_ids.value)

    def start(self):
        self.board.start_stream()

    def get_data(self, only_eeg=False, **kwargs):
        data = self.board.get_board_data(**kwargs)
        if only_eeg:
            data = data[self.eeg_channels, :]
        return data

    def get_data_async(self, **kwargs):
        ...

    def stop(self):
        if self.board.is_prepared():
            self.board.stop_stream()

    def exit(self):
        if self.board.is_prepared():
            # self.board.stop_stream()
            self.board.release_session()

    def __del__(self):
        self.exit()
