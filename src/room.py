import threading

# room contains the room type, occupancy and unique id. Each room stores its booking data.
class room:
    def __init__(self, floor, room_detail):
        try:
            self.id = "F" + str(floor) + "R" + str(room_detail["number"])
            self.room_type = room_detail["room_type"]
            self.occupancy = room_detail["occupancy"]
            self.calendar = {}
            self.lock = threading.Lock()
            print(f"{self.room_type} Room {self.id} is added.")
        except Exception as error:
            print("An error occurred in room():", error)

    def description(self):
        print(f"{self.room_type} Room {self.id} available with occupancy of {self.occupancy}\n")

    def book(self, startTime, endTime, date, bookingId):
        try:
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
        except Exception as error:
            print("An error occurred in room.book():", error)

    def cancel(self, date, startTime, endTime, bookingId):
        try:
            if self.calendar.get(date) != None:
                for i in range(startTime, endTime):
                    if self.calendar[date][i] == bookingId:
                        self.calendar[date][i] = 0
                    else:
                        print(f"System Notification ====> Wrong Information for Booking Id {bookingId}")
                        return False
                return True
            else:
                print(f"No Booking Found for Booking Id {bookingId}.")
                return False
        except Exception as error:
            print("An error occurred in room.cancel():", error)

    def is_available(self, date, startTime, endTime):
        try:
            if self.calendar.get(date) == None:
                return True
            appointments = self.calendar[date]
            # print(appointments)
            for i in range(startTime, endTime):
                if appointments[i]:
                    return False
            return True
        except Exception as error:
            print("An error occurred in room.is_available():", error)

    def listRoom(self, date):
        try:
            if self.calendar.get(date) == None:
                availability = "All Day"
            else:
                availability = self.calendar[date]
            return self, availability
        except Exception as error:
            print("An error occurred in room.listRoom():", error)

