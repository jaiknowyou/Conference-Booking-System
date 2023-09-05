import threading

class org:
    def __init__(self, id, name, contact):
        self.id = id
        self.name = name
        self.contact = contact
        self.user = []
        self.bookings = []
        self.limit = 30
        self.lock = threading.Lock()

    def renew_monthly_limit(self, limit):
        self.limit = limit
    
    def add_user(self, name, email, role, bookingPermission):
        self.user.append(user(name, email, role, self, bookingPermission))
        print(f"Current User is {name} and Current organisation is {self.name}")
        return self.user[-1]

    def notify(self):
        print(f"Organisation Notification ====> Hey, A user from your org {self.name} has made a booking.")

class user:
    def __init__(self, name, email, role, org, bookingPermission = False):
        self.id = "O" + str(org.id) + "U" + str(len(org.user))
        self.name = name
        self.email = email
        self.role = role
        self.org = org
        if bookingPermission:
            self.bookings = []
        
    def request_booking(self, room, date, startTime, endTime, booking):
        if self.bookings == None:
            print("User don't have booking Permissions.")
            return
        with self.org.lock:
            if self.org.limit == 0:
                print("Booking Limit has Reached. We cannot fulfill any bookings this month.")
            else:
                booking.lockBooking.acquire()
                bookingId = booking.generateId()
                if room.book(startTime, endTime, date, bookingId):
                    self.org.limit -= 1
                    booking.add_booking(bookingId, self.id, room.id, date, startTime, endTime)
                    self.bookings.append(bookingId)
                    self.notify()
                    self.org.bookings.append(bookingId)
                    self.org.notify()
                booking.lockBooking.release()

    def cancel_booking(self, bookingId):
        pass

    def notify(self):
        print(f"User Notification ====> Hey {self.name}, your booking is confirmed.")