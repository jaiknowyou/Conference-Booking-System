import threading
import datetime
import time

class testCase:
    def __init__(self, booking):
        try:
            self.booking = booking
            self.building = booking.building
        except Exception as error:
            print("An error occurred in testCase():", error)

# test Case 1: Adding Floor and conference room in the system. With the added description to User.
    def testCase1(self):
        try:
            print("testCase1 Result ====>")
            self.building.add_floor()
            self.building.add_room(0, "S", 2)
            self.building.add_room(2, "D", 12)
            self.building.add_room(2, "D", 20)
            self.building.add_room(1, "E", 10)
            self.building.add_room(3, "E", 5)
            self.building.add_room(4, "s", 10)
            self.building.description()
        except Exception as error:
            print("An error occurred in testCase1():", error)

# solution: The building description of floor and room would be printed

# test Case 2: Adding new Organisation and new User
    def testCase2(self):
        try:
            print("testCase2 Result ====>")
            self.booking.add_org("Varaha", "no-reply@varaha.co.in") # Register Org
            self.org = self.booking.get_org("no-reply@varaha.co.in") # searching Org by Unique Email id
            self.user = self.org.add_user("Admin", "admin@varaha.co.in", "Admin", True) # Register New user

            self.org2 = self.booking.add_org("Ctech", "no-reply@ctech.co.in")
            self.user2 = self.org2.add_user("Jai", "jai@ctech.co.in", "Admin", True)
            self.user3 = self.org2.add_user("Bhoomi", "bhoomi@ctech.co.in", "Admin", True)

            self.org3 = self.booking.add_org("AI Space", "no-reply@aispace.co.in")
            self.user4 = self.org3.add_user("Rahul", "jai@aispace.co.in", "Tech Support", True)

            self.org4 = self.booking.add_org("Treflo", "admin@treflo.com")
            self.user5 = self.org4.add_user("Jay Deva", "jay@aispace.so.in", "Dev Ops", True)
        except Exception as error:
            print("An error occurred in testCase2():", error)

# solution: User and Organisation would be added

# test Case 3: List Conference Rooms by date
    def testCase3(self):
        try:
            print("testCase3 Result ====>")
            date = datetime.date.today()
            self.building.listRoom(date)
        except Exception as error:
            print("An error occurred in testCase3():", error)

# solution: All rooms would be listed with the slot of availability for the given date

# test case 4: Find Suitable Room and Single Booking by User
    def testCase4(self):
        try:
            print("testCase4 Result ====>")
            startTime = 10
            endTime = 13
            date = datetime.date.today()
            available_slot = self.building.is_available({
                            "date": date,
                            "type": "E",
                            "occupancy": 4
                            }, startTime, endTime)
            self.user.request_booking(available_slot[0].id, date, startTime, endTime)
        except Exception as error:
            print("An error occurred in testCase4():", error)

# solution: A booking is made by the user and they should be notified.

# Advanced Test case
# test case 5: Same User requests booking same room on same date and time from two devices
    def testCase5(self):
        try:
            print("testCase5 Result ====>")
            startTime = 13
            endTime = 14
            date = datetime.date.today()
            listRoom = self.building.listRoom(date)
            thread1 = threading.Thread(target = self.user.request_booking, args = (listRoom[0].id, date, startTime, endTime))
            thread2 = threading.Thread(target = self.user.request_booking, args = (listRoom[0].id, date, startTime, endTime))
            thread1.start()
            thread2.start()
            thread1.join()
            thread2.join()
            self.building.listRoom(date)
        except Exception as error:
            print("An error occurred in testCase()5:", error)

# solution: One booking would be accepted and other booking would show room availability error.
# Room List would reflect booking status: Compare list before and after booking.

# test case 6: Two Users request booking same room on same date and time
    def testCase6(self):
        try:
            print("testCase6 Result ====>")
            startTime = 16
            endTime = 17
            date = datetime.date.today()
            listRoom = self.building.listRoom(date)
            thread1 = threading.Thread(target = self.user.request_booking, args = (listRoom[2].id, date, startTime, endTime))
            thread2 = threading.Thread(target = self.user2.request_booking, args = (listRoom[2].id, date, startTime, endTime))
            thread1.start()
            thread2.start()
            thread1.join()
            thread2.join()
            self.building.listRoom(date)
        except Exception as error:
            print("An error occurred in testCase6():", error)

# solution: user2 would not be able to book in this case. Only one booking would be made by a user.
# Room List would reflect booking status: Compare list before and after booking.

# test case 7: Multiple users request booking rooms on overlapping room and dates
    def testCase7(self):
        try:
            print("testCase7 Result ====>")
            startTime = 18
            endTime = 20
            date = datetime.date.today()
            listRoom = self.building.listRoom(date)
            thread1 = threading.Thread(target = self.user2.request_booking, args = (listRoom[2].id, date, startTime, endTime))
            # thread1 =====> 18-20 hrs today booking by user2 
            startTime = startTime + 1
            thread2 = threading.Thread(target = self.user.request_booking, args = (listRoom[2].id, date, startTime, endTime))
            # thread2 =====>  19-20 hrs today same room booking by user
            date = date + datetime.timedelta(days = 1)
            thread3 = threading.Thread(target = self.user3.request_booking, args = (listRoom[2].id, date, startTime, endTime))
            # thread3 =====>  19-20 hrs tommorow booking by user3
            thread4 = threading.Thread(target = self.user4.request_booking, args = (listRoom[0].id, date, startTime, endTime))
            # thread4 =====>  19-20 hrs tommorow different room booking by user4
            thread1.start()
            thread2.start()
            thread3.start()
            thread4.start()
            thread1.join()
            thread2.join()
            thread3.join()
            thread4.join()
            self.building.listRoom(date - datetime.timedelta(days = 1))
            self.building.listRoom(date)
        except Exception as error:
            print("An error occurred in testCase7():", error)

# solution: user2, user3 and user4 should be able to book in this case. Only one booking would be rejected due to overlaping time of booking the same room. 
# Room List would reflect booking status: Compare list before and after booking.

# test case 8: User requests to book a room for next 30 days at secific time.  Case of Monthly Booking Limit
    def testCase8(self):
        try:
            print("testCase8 Result ====>")
            startTime = 17
            endTime = 18
            date = datetime.date.today()
            for _ in range(30):
                date = date + datetime.timedelta(days = 1)
                thread = threading.Thread(target = self.user.request_booking, args = ("F2R1", date, startTime, endTime))
                thread.start()
        except Exception as error:
            print("An error occurred in testCase()8:", error)

# solution: user should be able to book upto 28 bookings. Last 3 bookings would be rejected due to monthly booking limit of Organisation.

# test case 9: User requests booking for past date and time.
    def testCase9(self):
        try:
            print("testCase9 Result ====>")
            startTime = 0
            endTime = 1
            date = datetime.date.today()
            listRoom = self.building.listRoom(date)
            thread = threading.Thread(target = self.user2.request_booking, args = (listRoom[0].id, date, startTime, endTime))
            # thread =====> 0-1 hrs today booking request by user (past time)
            thread2 = threading.Thread(target = self.user2.request_booking, args = (listRoom[0].id, date - datetime.timedelta(days = 5), startTime, endTime))
            # thread2 =====> 0-1 hrs 5 days ago booking request by user (past date) 
            thread.start()
            thread2.start()
        except Exception as error:
            print("An error occurred in testCase9():", error)

# solution: Both bookings (thread and thread2) would be rejected due to past date time.

# test case 10: A booking is cancelled by a user. Another user tries to book that room after slots get free.
    def testCase10(self):
        try:
            print("testCase10 Result ====>")
            self.user2.get_bookings(datetime.date.today())
            last_bookingId = self.user2.bookings[-1]
            print(last_bookingId)
            thread = threading.Thread(target = self.user2.cancel_booking, args = (last_bookingId, ))
            thread.start()
            thread.join()
            self.user2.get_bookings(datetime.date.today())
        except Exception as error:
            print("An error occurred in testCase10():", error)

# solution: The latest booking of User2 would show status as Cancelled.

# test case 11: A user able to access other user booking of the same organisation and different Organisation.
    def testCase11(self):
        try:
            print("testCase11 Result ====>")
            date = datetime.date.today()
            self.user2.get_bookings(date, self.user3.id)
            time.sleep(1)
            print("")
            self.user2.org.get_bookings(date)
            time.sleep(1)
            print("")
            self.user2.get_bookings(date, self.user.id)
        except Exception as error:
            print("An error occurred in testCase11():", error)

# solution: User2 would be able to see user3 booking and then organisation booking but not any other bookings.

# test case 12: Modify booking permission and Check booking for user without booking permission
    def testCase12(self):
        try:
            print("testCase12 Result ====>")
            self.org4.modifyPermissions(self.user5)
            self.user5.request_booking("F3R1", datetime.date.today(), 9, 11)
            print("")
            time.sleep(1)
            self.org4.modifyPermissions(self.user5)
            self.user5.request_booking("F3R1", datetime.date.today(), 20, 24)
        except Exception as error:
            print("An error occurred in testCase12():", error)

# solution: user5 would be able to get booking once only as the booking permissions were revoked.

# test case 13: A user tries to cancel booking within 15 minutes of the booking time slot. (to be manually checked)
    def testCase13(self):
        try:
            print("testCase13 Result ====>")
            startTime = datetime.datetime.now().hour + 1
            self.user5.request_booking("F1R1", datetime.date.today(), startTime, startTime + 1)
            time.sleep(1)
            self.user5.cancel_booking(self.user5.bookings[-1])
        except Exception as error:
            print("An error occurred in testCase13():", error)

# solution: user5 would not be able to cancel booking if the next hour is within 15 minutes.
