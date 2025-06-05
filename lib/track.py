class tracker:
    def __init__(self):
        self.track_list = []
    def add_track(self,track):
        self.track_list.append(track)
    def history(self):
        return self.track_list