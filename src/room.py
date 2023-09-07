import threading

# room contains the room type, occupancy and unique id. Each room stores its booking data.
class room:
    def __init__(self, floor, room_detail):
        try:
            # A unique id has info about floor and room number
            self.id = "F" + str(floor) + "R" + str(room_detail["number"])
            self.room_type = room_detail["room_type"]
            self.occupancy = room_detail["occupancy"]
            # Using Calendar as dictionary to store date specific booking data
            self.calendar = {}
            # Lock while booking the room so that only one thread is using the function to book
            self.lock = threading.Lock()
            print(f"{self.room_type} Room {self.id} is added.")
        except Exception as error:
            print("An error occurred in room():", error)

    def description(self):
        print(f"{self.room_type} Room {self.id} available with occupancy of {self.occupancy}\n")

    def book(self, startTime, endTime, date, bookingId):
        try:
            # Thread Lock to ensure one booking at a time of the room
            with self.lock:
                if self.is_available(date, startTime, endTime):
                    # initialising calendar key - value as 24 hour slot against date as a key
                    if self.calendar.get(date) == None:
                        self.calendar[date] = [0 for i in range(24)]
                    for i in range(startTime, endTime):
                        # Storing bookingId which is non-zero value implying room is booked
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
                        # booking cancellation through updating calendar slots.
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
            # if room is available on Given Date-Time Slot return True else False
            if self.calendar.get(date) == None:
                return True
            appointments = self.calendar[date]
            for i in range(startTime, endTime):
                if appointments[i]:
                    return False
            return True
        except Exception as error:
            print("An error occurred in room.is_available():", error)

    def listRoom(self, date):
        # Listing all rooms with availability on given date
        try:
            if self.calendar.get(date) == None:
                availability = "All Day"
            else:
                availability = self.calendar[date]
            return self, availability
        except Exception as error:
            print("An error occurred in room.listRoom():", error)

