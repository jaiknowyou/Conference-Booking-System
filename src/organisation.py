import threading
import datetime
import re

# Keeping all the organisation related data, user data and functionality to view and modify booking Permissions.
class org:
    def __init__(self, bookingSystem, id, name, contact):
        try:
            self.id = id
            self.name = name
            self.contact = contact
            self.user = []
            self.bookingSystem = bookingSystem
            self.bookings = []
            self.limit = 30
            self.lock = threading.Lock()
        except Exception as error:
            print("An error occurred in org():", error)

    def renew_monthly_limit(self, limit):
        self.limit = limit
    
    def add_user(self, name, email, role, bookingPermission):
        try:
            self.user.append(user(name, email, role, self, bookingPermission))
            print(f"Current User is {name} and Current organisation is {self.name}")
            return self.user[-1]
        except Exception as error:
            print("An error occurred in org.add_user():", error)

    def notify(self):
        print(f"Organisation Notification ====> Hey, A user from your org {self.name} has made a booking.")

    @staticmethod
    def display_bookings(bookings):
        try:
            print(f"    Booking Id      Room Id      Date      StartTime      EndTime      Status      Booked on      Booked by (User Id)")
            for i in range(0, len(bookings)):
                active = "Reserved" if bookings[i].active else "Cancelled"
                print(f"{i+1}.      {bookings[i].id}            {bookings[i].roomId}      {bookings[i].date}        {bookings[i].startTime}:00      {bookings[i].endTime}:00    {active}        {bookings[i].dateOfBooking}         {bookings[i].userId}")
        except Exception as error:
            print("An error occurred in org.display_booking():", error)

    def show_bookings(self, date, bookingIds = None):
        try:
            bookings = []
            if bookingIds == None:
                print(f"Bookings Done by {self.name}:")
                bookingIds = self.bookings
            for i in range(len(bookingIds)-1, -1, -1):
                bookingId = bookingIds[i]
                info = self.bookingSystem.getDetail(bookingId)
                if info.date < date:
                    break
                else:
                    bookings.append(info)
            org.display_bookings(bookings)
            return bookings
        except Exception as error:
            print("An error occurred in org.show_bookings():", error)

    def modifyPermissions(self, user):
        if user.bookings == None:
            user.bookings = []
        else:
            user.bookings = None

# Keeping all the user related data, functionality to get, cancel bookings and notify User.
class user:
    def __init__(self, name, email, role, org, bookingPermission):
        try:
            self.id = "O" + str(org.id) + "U" + str(len(org.user))
            self.name = name
            self.email = email
            self.role = role
            self.org = org
            if bookingPermission:
                self.bookings = []
        except Exception as error:
            print("An error occurred in user():", error)
        
    def request_booking(self, room, date, startTime, endTime):
        try:
            if startTime < 0 or startTime > 23 or endTime < 1 or endTime > 24 or endTime < startTime:
                print("Invalid time range.")
                return
            if self.bookings == None:
                print("User don't have booking Permissions.")
                return
            elif datetime.datetime(date.year, date.month, date.day, startTime) < datetime.datetime.today():
                print("Invalid date. Reservation Date has already Passed.")
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
        except Exception as error:
            print("An error occurred in user.request_booking():", error)

    def cancel_booking(self, bookingId):
        try:
            if bookingId in self.bookings:
                info = self.org.bookingSystem.getDetail(bookingId)
                if not info.active:
                    print("Booking has been already cancelled.")
                    return
                elif info.date == datetime.date.today():
                    timediff = datetime.datetime(info.date.year, info.date.month, info.date.day, info.startTime) - datetime.datetime.now()
                    if divmod(timediff.total_seconds(), 60)[0] < 15.0:
                        print("Booking cannot be cancelled within 15 minutes of the reservation time.")
                        return
                elif info.date < datetime.date.today():
                    print("Reservation date has been passed for this booking.")
                    return
                room = self.org.bookingSystem.building.searchRoom(info.roomId)
                if room.cancel(info.date, info.startTime, info.endTime, bookingId):
                    self.org.bookingSystem.changeStatus(bookingId)
                    self.org.limit += 1
                    self.notify(3)
            else:
                print("User has no booking with this booking Id.")
        except Exception as error:
            print("An error occurred in user.cancel_booking():", error)

    def show_bookings(self, date, userId = None):
        try:
            if userId:
                numbers = re.findall(r'\d+', userId)
                [o, u ]= [int(num) for num in numbers]
                if len(self.org.user) > u and self.org.user[u].id == userId:
                    print(f"Bookings Done by {self.org.user[u].name}:")
                    return self.org.show_bookings(date, self.org.user[u].bookings)
                else:
                    print("User Not Found.")
            else:
                print(f"Bookings Done by {self.name}:")
                return self.org.show_bookings(date, self.bookings)
        except Exception as error:
            print("An error occurred in user.show_bookings():", error)

    def notify(self, mtype = 1):
        if mtype == 1:
            print(f"User Notification ====> Hey {self.name}, your booking is confirmed.")
        elif mtype == 2:
            print(f"User Notification ====> Hey {self.name}, The room is not available at this date time.")
        else:
            print(f"User Notification ====> Booking Cancelled Successfully.")