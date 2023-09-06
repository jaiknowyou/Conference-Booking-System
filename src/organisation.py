import threading
import datetime

class org:
    def __init__(self, bookingSystem, id, name, contact):
        self.id = id
        self.name = name
        self.contact = contact
        self.user = []
        self.bookingSystem = bookingSystem
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

    @staticmethod
    def display_bookings(bookings):
        print(f"    Booking Id      Room Id      Date      StartTime      EndTime      Status      Booked on      Booked by (User Id)")
        for i in range(0, len(bookings)):
            bookings[i].active = "Reserved" if bookings[i].active else "Cancelled"
            print(f"{i+1}.      {bookings[i].id}            {bookings[i].roomId}      {bookings[i].date}        {bookings[i].startTime}:00      {bookings[i].endTime}:00    {bookings[i].active}        {bookings[i].dateOfBooking}         {bookings[i].userId}")

    def show_bookings(self, date, bookingIds = None):
        bookings = []
        if bookingIds == None:
            print(f"Bookings Done by {self.name}:")
            bookingIds = self.bookings
        else:
            print("Bookings Done by User:")
        for i in range(len(bookingIds)-1, -1, -1):
            bookingId = bookingIds[i]
            info = self.bookingSystem.getDetail(bookingId)
            if info.date < date:
                break
            else:
                bookings.append(info)
        org.display_bookings(bookings)
        return bookings

class user:
    def __init__(self, name, email, role, org, bookingPermission = False):
        self.id = "O" + str(org.id) + "U" + str(len(org.user))
        self.name = name
        self.email = email
        self.role = role
        self.org = org
        if bookingPermission:
            self.bookings = []
        
    def request_booking(self, room, date, startTime, endTime):
        if self.bookings == None:
            print("User don't have booking Permissions.")
            return
        with self.org.lock:
            if self.org.limit == 0:
                print("Booking Limit has Reached. We cannot fulfill any bookings this month.")
            else:
                if type(room) == str:
                    room = self.org.bookingSystem.building.searchRoom(room)
                self.org.bookingSystem.lockBooking.acquire()
                bookingId = self.org.bookingSystem.generateId()
                if room.book(startTime, endTime, date, bookingId):
                    self.org.limit -= 1
                    self.org.bookingSystem.add_booking(bookingId, self.id, room.id, date, startTime, endTime)
                    self.bookings.append(bookingId)
                    self.notify()
                    self.org.bookings.append(bookingId)
                    self.org.notify()
                else:
                    self.notify(2)
                self.org.bookingSystem.lockBooking.release()

    def cancel_booking(self, bookingId):
        if bookingId in self.bookings:
            info = self.org.bookingSystem.getDetail(bookingId)
            if not info.active:
                print("Booking has been already cancelled.")
            elif info.date == datetime.date.today():
                timediff = datetime.datetime(info.date.year, info.date.month, info.date.day, info.startTime) - datetime.datetime.now()
                if divmod(timediff.total_seconds(), 60)[0] < 15.0:
                    print("Booking cannot be cancelled within 15 minutes of the reservation time.")
                    return
            elif info.date < datetime.date.today():
                print("Reservation date has been passed for this booking.")
            else:
                room = self.org.bookingSystem.building.searchRoom(info.roomId)
                if room.cancel(info.date, info.startTime, info.endTime, bookingId):
                    self.org.bookingSystem.changeStatus(bookingId)
                    self.org.limit += 1
                    self.notify(3)
        else:
            print("User has no booking with this booking Id.")

    def show_bookings(self, date):
        return self.org.show_bookings(date, self.bookings)

    def notify(self, mtype = 1):
        if mtype == 1:
            print(f"User Notification ====> Hey {self.name}, your booking is confirmed.")
        elif mtype == 2:
            print(f"User Notification ====> Hey {self.name}, The room is not available at this date time.")
        else:
            print(f"User Notification ====> Booking Cancelled Successfully.")