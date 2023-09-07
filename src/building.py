from src.floor import floor
import re
import datetime

# building represents Conference Room building which stores the data related to different floors.
# This acts as a basic interface to get room availability data and changing building structure.
class building:
    def __init__(self, nfloor):
        try:
            self.building = []
            for _ in range(nfloor):
                self.building.append(floor(len(self.building)))
        except Exception as error:
            print("An error occurred in building():", error)

    def add_floor(self):
        # Adding one more floor on Building
        try:
            self.building.append(floor(len(self.building)))
            print(f"One more Floor is added. Total number of floors in buildings are {len(self.building)}")
        except Exception as error:
            print("An error occurred in building.add_floor():", error)

    def add_room(self, nfloor, room_type, occupancy):
        # Adding one more room on given floor with room type and room capacity
        try:
            if nfloor >= len(self.building):
                print("Invalid Floor.")
            self.building[nfloor].add_room({"room_type": room_type, "occupancy": occupancy, "number":len(self.building[nfloor].room)+1})
        except Exception as error:
            print("An error occurred in building.add_room():", error)

    def description(self):
        try:
            print(f"The building has total {len(self.building)} floors.")
            for i in self.building:
                i.description()
        except Exception as error:
            print("An error occurred in building.decription():", error)

    def searchRoom(self, roomId):
        # Getting room Obj by specific id
        try:
            numbers = re.findall(r'\d+', roomId)
            [f, r ]= [int(num) for num in numbers]
            return self.building[f].room[r-1]
        except Exception as error:
            print("An error occurred in building.searchRoom():", error)

    def is_available(self, req, start, end):
        try:
            if start < 0 or start > 23 or end < 1 or end > 24 or end < start:
                print("Invalid time range.")
                return
            slots = []
            for i in self.building:
                # checking room availability on each floor
                room = i.is_available(req, start, end)
                if room:
                    slots = slots + room
            print("  Floor & Room No.    Type    Occupancy")
            for i in range(0, len(slots)):
                print(f"{i+1}. {slots[i].id}                {slots[i].room_type}         {slots[i].occupancy}")
            return slots
        except Exception as error:
            print("An error occurred in building.is_available():", error)

    def listRoom(self, date):
        # Listing all rooms with availability
        try:
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
                        # available = "All Day"
                    else:
                        # Checking Available time range for the room and appending them in List
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
        except Exception as error:
            print("An error occurred in building.listRoom():", error)

