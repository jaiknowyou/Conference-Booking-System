from floor import floor
import re
import datetime

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
        print("  Floor & Room No.    Type    Occupancy")
        for i in range(0, len(slots)):
            print(f"{i+1}. {slots[i].id}                {slots[i].room_type}         {slots[i].occupancy}")
        return slots

    def listRoom(self, date):
        if date < datetime.date.today():
            print("Sorry, The date is Invalid.")
            return ()
        else:
            listRooms = ()
            for i in self.building:
                listRooms = listRooms + i.listRoom(date)
            print(f" Floor & Room No.    Capacity    Type    Available Slot hours ({date})")
            for i in range(0, len(listRooms), 2):
                if type(listRooms[i+1]) == str:
                    available =  listRooms[i+1]
                else:
                    available = []
                    j = 0
                    while j < 24:
                        while j < 24 and listRooms[i+1][j]:
                            j+=1
                        s = j
                        while j < 24 and not listRooms[i+1][j]:
                            j += 1
                        if s != 24:
                            available.append(str(s)+" to "+str(j))
                print(f"{int(i/2+1)}.    {listRooms[i].id}             {listRooms[i].occupancy}          {listRooms[i].room_type}         {available}")
            return listRooms

