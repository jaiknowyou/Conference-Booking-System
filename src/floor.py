from room import room

class floor:
    def __init__(self, number):
        self.number = number
        self.room = []

    def total_room(self):
        return len(self.room)

    def description(self):
        print(f"Floor Number {self.number} has {self.total_room()} room(s):")
        for hall in self.room:
            hall.description()

    def add_room(self, room_type):
        self.room.append( room(self.number, room_type))

    def is_available(self, req, start, end):
        slots = []
        filtered = filter(lambda x: x.room_type == req["type"] and x.occupancy >= req["occupancy"], self.room)
        for hall in filtered:
            available_slot = hall.is_available(req["date"], start, end)
            if available_slot:
                slots.append(hall)
                hall.description()
        return slots
