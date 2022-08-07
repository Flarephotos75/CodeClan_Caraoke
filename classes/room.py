class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.rooms = []
        self.guestlist = []
        
    def add_a_room(self, room):
        self.rooms.append(room)
        return len(self.rooms)
        
    def add_guest_to_room(self, guest, roomname):
        self.guestlist.append(guest)
        self.guests = self.guestlist
        if len(self.guestlist) == 0:
            return "No guests in room"
        if len(self.guestlist) == 1:
            return (f"{self.guests[0]} is in room {roomname.name}")
        else:
            if len(self.guestlist) > 1:
                return (f"{self.guests[0]} and {self.guests[1]} are in room {roomname.name}")
        
    def remove_guest_from_room(self, guest):
        self.guestlist.remove(guest)
        return len(self.guestlist)
    
    def room_capacity_checker(self, room):
        self.roomcap = room.capacity
        print(self.roomcap)
        print(self.guestlist)
        if self.roomcap - len(self.guestlist) > 0:
            self.can_take_guests = True
            print(self.roomcap)            
            return self.can_take_guests
        return False