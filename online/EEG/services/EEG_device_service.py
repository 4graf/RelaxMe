from brainflow import BrainFlowInputParams, BoardShim, BoardIds


class EEGDevice:

    def __init__(self, board_ids=BoardIds.CYTON_BOARD):
        params = BrainFlowInputParams()
        params.serial_port = 'COM3'

        self.board = BoardShim(BoardIds.SYNTHETIC_BOARD, params)
        # self.board = BoardShim(board_ids, params)
        self.board.prepare_session()

        self.sampling_rate = self.board.get_sampling_rate(board_ids)
        self.channel_names = self.board.get_eeg_names(board_ids)
        self.eeg_channels = BoardShim.get_eeg_channels(board_ids.value)

    def get_data(self, **kwargs):
        return self.board.get_board_data(**kwargs)

    def start(self):
        self.board.start_stream()

    def stop(self):
        if self.board.is_prepared():
            self.board.stop_stream()
            self.board.release_session()

    def __del__(self):
        self.stop()
