import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def test_add_a_song(self):
        self.song1 = Song("The Pretender", "Foo Fighters")
        self.song2 = Song("Plug in Baby", "Muse")
        self.song1.add_a_song(self.song1)
        self.song2.add_a_song(self.song2)
        