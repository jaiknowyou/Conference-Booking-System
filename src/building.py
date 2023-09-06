from floor import floor
import re
class building:
    def __init__(self, nfloor):
        self.building = []
        for i in range(nfloor):
            self.building.append(floor(len(self.building)))

    def add_floor(self):
        self.building.append(floor(len(self.building)))
        print(f"One more Floor is added. Total number of floors in buildings are {len(self.building)}")

    def add_room(self, nfloor, room_type, occupancy):
        if nfloor >= len(self.building):
            print("Invalid Floor.")
        self.building[nfloor].add_room({"room_type": room_type, "occupancy": occupancy, "number":self.building[nfloor].total_room()+1})

    def description(self):
        print(f"The building has total {len(self.building)} floors.")
        for i in self.building:
            i.description()

    def searchRoom(self, roomId):
        numbers = re.findall(r'\d+', roomId)
        [f, r ]= [int(num) for num in numbers]
        return self.building[f].room[r-1]

    def is_available(self, req, start, end):
        slots = []
        for i in self.building:
            room = i.is_available(req, start, end)
            if room:
                slots = slots + room
        return slots

    def listRoom(self, date):
        rooms = ()
        for i in self.building:
            rooms = rooms + i.listRoom(date)
        return rooms

