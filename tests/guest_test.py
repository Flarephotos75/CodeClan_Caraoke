import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Steven", 100, "Plug in Baby")
        self.guest2 = Guest("Kathleen", 15, "The Pretender")
        self.guest3 = Guest("Aiden", 150, "Shotgun")
        self.guests = []
        
    def test_guest_name(self):
        self.assertEqual("Steven", self.guest1.name)

    def test_wallet_amount(self):
        self.assertEqual(100, self.guest1.wallet)

    def test_reduce_wallet(self):
        self.guest1.reduce_wallet(10)
        self.assertEqual(90, self.guest1.wallet)
    