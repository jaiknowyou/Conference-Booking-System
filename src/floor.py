from src.room import room

# floor stores Conference Room which stores the data related to different rooms on the floor.
class floor:
    def __init__(self, number):
        try:
            self.number = number
            self.room = []
        except Exception as error:
            print("An error occurred in floor():", error)

    def description(self):
        try:
            print(f"Floor Number {self.number} has {len(self.room)} room(s):")
            for hall in self.room:
                hall.description()
        except Exception as error:
            print("An error occurred in floor.description():", error)

    def add_room(self, room_type):
        try:
            self.room.append( room(self.number, room_type))
        except Exception as error:
            print("An error occurred in floor.add_room():", error)

    def is_available(self, req, start, end):
        try:
            slots = []
            # Filtering room based on user requirement
            filtered = filter(lambda x: x.room_type == req["type"] and x.occupancy >= req["occupancy"], self.room)
            for hall in filtered:
                # checking each room availability on given date time
                available_slot = hall.is_available(req["date"], start, end)
                if available_slot:
                    slots.append(hall)
            # Returning available rooms
            return slots
        except Exception as error:
            print("An error occurred in floor.is_available():", error)

    def listRoom(self, date):
        # Listing all rooms
        try:
            rooms = ()
            for i in self.room:
                rooms = rooms + i.listRoom(date)
            return rooms
        except Exception as error:
            print("An error occurred in floor.listRoom():", error)
