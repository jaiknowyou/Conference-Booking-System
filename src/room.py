import threading

class room:

    def __init__(self, floor, room_detail):
        self.id = "F" + str(floor) + "R" + str(room_detail["number"])
        self.room_type = room_detail["room_type"]
        self.occupancy = room_detail["occupancy"]
        self.calendar = {}
        self.lock = threading.Lock()
        print(f"{self.room_type} Room {self.id} is added.")

    def description(self):
        print(f"{self.room_type} Room {self.id} available with occupancy of {self.occupancy}\n") 

    def book(self, startTime, endTime, date, bookingId):
        with self.lock:
            if self.is_available(date, startTime, endTime):
                if self.calendar.get(date) == None:
                    self.calendar[date] = [0 for i in range(24)]
                for i in range(startTime, endTime):
                    self.calendar[date][i] = bookingId
                print(f"System Notification ====> Room {self.id} has booked for {date} from {startTime}:00 to {endTime}:00 hrs with booking Id {bookingId}.")
                return True
            else:
                print(f"System Notification ====> This Room is not available for booking.")
                return False

    def is_available(self, date, startTime, endTime):
        if self.calendar.get(date) == None:
            return True
        appointments = self.calendar[date]
        # print(appointments)
        for i in range(startTime, endTime):
            if appointments[i]:
                return False
        return True

