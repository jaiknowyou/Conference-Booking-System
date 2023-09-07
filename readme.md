
# A Conference Room Booking System

To get the code running, please download the repo and run main.py using python3 version,
For running test case type "t" and enter.
Type enter to run consecutive test cases.

## Features

This program is a basic Room Bookingn system. A Conferece building can be defined with any number of rooms of 3 different types: Standard, Deluxe, Executive (varying facilities). The important features are:

1. Any number of users can be added and stored in the system. Each organisation has users which can create/cancel a booking.

2. Each room has a calendar that keeps track of bookings. Calendar can be availed to book room today or any day after today. the limit for booking in future is not set.

3. Reservations can be cancelled. cancelled reservation data would still be available.

4. The program provides the user functionality to get list of rooms are available on the selected dates, along with the range of booking hours possible (within 24 hours at a given date).

5. Past bookings of users and organisation can be fetched by the user of that organisation.

6. Multiple Users from different organisation can book any room at any time. All booking operations maintain data integrity and are thread safe operations.
Note: threading is used for multiple user booking at the same time.

Features Which can be added by small modifications:

1. The booking system is losely coupled with Conference Rooms. This means multiple conference buildings can be used with the slight modification.

2. If the user inputs incorrect values or data types, there is an error message provided, however the function has to be re-initialized again. However to avoid this happening, the program provides prompts throughout in manual mode via command line.

3. If 2 users/organisations inputs the same email id, duplicate users/organisations are created, however This can be eliminated by using dictionary as data structure.

4. A price tag could be added specific to each room which can be set according to occupancy and room type. The program can also use strategy pattern to keep price dynamic.

## Code Description

The Booking System has many Subjects:
1. Building = Floor and Rooms
    class represntation: 
        building
        floor
        room
2. Organisations and Users
    class represntation:
        org
        user

3. Next is Interaction between Users and Rooms which is implemented by action like booking room, cancellation of booking at given reservation time
    Actions/ Functions ():
        user.request_booking()
        user.cancel_booking()
        room.book()
        room.cancel()

4. All data related to booking is linked with:
    class:
        bookingSystem
    which are reservations, userId, roomId, reservation date and time, booking date

5. Reservation data is saved in its own room Object:
    room.calendar which is initialised as 
        map[date] = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
        key: date
        value: list representing 24 hours
        the value 0 represents the hourly empty slot

## Edge Cases Covered:

Basic Test Cases:

test Case 1: Adding Floor and conference room in the system. With the added description to User.

test Case 2: Adding new Organisation and new User

test Case 3: List Conference Rooms by date

test case 4: Find Suitable Room and Single Booking by User

Advanced Test Cases:

test case 5: Same User requests booking same room on same date and time from two devices

test case 6: Two users request booking same room on same date and time

test case 7: Multiple users booking rooms on overlapping room and dates

test case 8: User requests to book a room for next 30 days at secific time. Case of Monthly Booking Limit

test case 9: User requests booking for past date and time.

test case 10: A booking is cancelled by a user. Another user tries to book that room after slots get free.

test case 11: A user able to access other users booking and organisation booking.

test case 12: Modify booking permission and Check booking for user without booking permission

test case 13: A user tries to cancel booking within 15 minutes of the booking time slot ===> [to be manually checked]

###

Steps Followed

Step 1: Add Floor and Room
    Add floor
        floor number
        array of room object = initialise empty room array
        add room - require room detail, calender
    room object
        room number
        floor number
        occupancy
        calender
        room type

Step 2: main.py
    Add floor Object and Room Object

Step 3: Add Organisation and User
    Only user can book based on permission

Step 4 & 5: filter Available slots (diff params)

Step 4 & 5: Booking Request through user

Step 6: Booked slots of organisation and user

Step 7: cancel specific slots

Step 8: Monthly booking Limit on month Renew

Step 9: Completing Test Cases

Step 10: Write Solution of test Cases

Step 11: Commenting - Description

Step 12: Documentation = readme.md