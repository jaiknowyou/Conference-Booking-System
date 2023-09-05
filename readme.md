Issues:
# Monthly Limit = Lock ----> solved
# reservation Id unique ----> solved
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

Step 4 & 5: Booking Request through user

Step 4 & 5: filter Available slots (diff params)

Step 6: Booked slots of organisation and user

Step 7: cancel specific slots

Step 8: Monthly booking Limit on month Renew


While Booking what do you require:
bookingId = Adjacent room Id, reservation date, time slots, userId

Write Test Cases:

1. Two Users booking same room on same date and different time slots
2. Two users booking same room on same date and time
3. Two users booking same room on different dates
4. Two users booking different rooms on same datetime
5. Monthly booking limit of org is 1. Two users are trying to book
6. A user tries to do double booking.
7. A booking is cancelled by a user. Another user tries to book that room after slots get free.
8. A user tries to cancel booking within 15 minutes of the booking time slot.
9. Two bookings have been added simultaneously from the same org. Check booking id.
10. Two users from same organisation and third from different org does booking.
11. Check booking for user without booking permission

Lock booking when overlaping datetime and same room.

