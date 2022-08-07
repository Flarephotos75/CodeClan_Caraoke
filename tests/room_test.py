import unittest
from classes.room import Room
from classes.song import *
from classes.guest import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Steven", 100, "Plug in Baby")
        self.guest2 = Guest("Kathleen", 15, "The Pretender")
        self.guest3 = Guest("Aiden", 100, "Shotgun")
        self.guest4 = Guest("Mandy", 15, "Iris")
        self.guest5 = Guest("Claire", 100, "Aga Do Do Do")
        self.guest6 = Guest("Amy", 15, "Crazy Nights")
        self.song1 = Song("The Pretender", "Foo Fighters")
        self.song2 = Song("Plug in Baby", "Muse")
        self.songlist = Song("Shotgun", "George Ezra")
    
    def test_create_a_room(self):
        self.room1 = Room("Kurgen", 5)
        self.roomcount = self.room1.add_a_room(self.room1)
        self.assertEqual(self.roomcount, 1)
        
    def test_add_guest_to_room(self):
        self.room1 = Room("Kurgen", 5)
        result = self.room1.add_guest_to_room(self.guest1.name, self.room1)
        self.assertEqual(result, "Steven is in room Kurgen")
        
    def test_add_multiple_guests_to_room(self):
        self.room1 = Room("Kurgen", 5)
        result = self.room1.add_guest_to_room(self.guest1.name, self.room1)
        result = self.room1.add_guest_to_room(self.guest2.name, self.room1)
        self.assertEqual(result, "Steven and Kathleen are in room Kurgen")
        
    def test_remove_guest_from_room(self):
        self.room1 = Room("Kurgen", 5)
        self.room1.add_guest_to_room(self.guest1, self.room1)
        self.room1.add_guest_to_room(self.guest2.name, self.room1)
        self.room1.remove_guest_from_room(self.guest1)
        result = len((self.room1.guestlist))
        self.assertEqual(result, 1)
        
    def test_add_songs_to_room(self):
        self.songlist.songs.append(self.song1)
        self.songlist.songs.append(self.song2)
        self.assertEqual(2, len(self.songlist.songs))
        
    def test_check_room_capacity(self):
        self.cap = Room("Kurgen", 5)
        self.capcheck = self.cap.room_capacity_checker(self.cap)
        self.assertEqual(True, self.cap.can_take_guests)
        
    def test_add_guests_if_room_capacity_is_low(self):
        self.cap = Room("Kurgen", 5)
        self.capcheck = self.cap.room_capacity_checker(self.cap)
        self.cap.guestlist.append(self.guest1)
        self.cap.guestlist.append(self.guest2)
        self.cap.guestlist.append(self.guest3)
        self.cap.guestlist.append(self.guest4)
        self.cap.guestlist.append(self.guest5)
        self.cap.guestlist.append(self.guest6)
        self.cap.add_guest_to_room(self.guest1.name, self.cap)
        self.cap.add_guest_to_room(self.guest2.name, self.cap)
        self.cap.add_guest_to_room(self.guest3.name, self.cap)
        self.cap.add_guest_to_room(self.guest4.name, self.cap)
        self.cap.add_guest_to_room(self.guest5.name, self.cap)
        self.cap.add_guest_to_room(self.guest6.name, self.cap)
        if self.capcheck:
            self.cap.add_guest_to_room(self.guest1.name, self.cap)
            self.cap.add_guest_to_room(self.guest2.name, self.cap)
        self.assertEqual(True, self.cap.can_take_guests)