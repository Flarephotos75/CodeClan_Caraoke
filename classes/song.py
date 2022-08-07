class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.songs = []
        
    def add_a_song(self, song):
        self.songs.append(song)