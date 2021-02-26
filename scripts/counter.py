class Counter:
    def __init__(self, fps, start_beat=0):
        self.bpm = fps
        self.k = start_beat

    def counter(self):
        self.k = self.k + 1 if self.k < self.bpm else 0

    def get_counter(self):
        return self.k

    def get_bpm(self):
        return self.bpm
