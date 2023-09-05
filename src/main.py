import threading

from building import building
# from organisation import org
from booking import bookingSystem
import datetime

building = building(3)
booking = bookingSystem("VARAHA CONFERENCE OFFICES")

building.add_room(0, "S", 2)
building.add_room(2, "D", 12)
building.add_room(1, "E", 10)
building.description()

if datetime.date.today().day == 1:
    booking.renew_monthly_limit()


booking.add_org("Varaha","no-reply@varaha.co.in")
org = booking.get_org("no-reply@varaha.co.in")
user = org.add_user("Admin","admin@varaha.co.in", "Admin", True)
org.renew_monthly_limit(2)

booking.add_org("Ctech","no-reply@ctech.co.in")
org2 = booking.get_org("no-reply@ctech.co.in")
user2 = org2.add_user("Jai","jai@ctech.co.in", "Admin", True)

booking.add_org("AI Space","no-reply@aispace.co.in")
org3 = booking.get_org("no-reply@aispace.co.in")
user3 = org3.add_user("Rahul","jai@aispace.co.in", "Tech Support", True)

date = datetime.date(2023, 9, 9)
s = 13
e = 15
available_slot = building.is_available({
    "date": date,
    "type": "D",
    "occupancy": 4
}, s, e)

print("  Floor & Room No.    Type    Occupancy")
for i in range(0, len(available_slot)):
    print(f"{i+1}. {available_slot[i].id}                 {available_slot[i].room_type}          {available_slot[i].occupancy}")
print("Select Room by Choosing index:")
num = int(input())
user.request_booking(available_slot[i-1], date, s, e, booking)
thread1 = threading.Thread(target = user3.request_booking, args = (available_slot[i-1], date, s, e, booking))
s = 2
e = 3
thread2 = threading.Thread(target = user2.request_booking, args = (available_slot[i-1], date, s, e, booking))
s = 6
e = 7
thread3 = threading.Thread(target = user.request_booking, args = (available_slot[i-1], date, s, e, booking))
thread3.start()
thread2.start()
thread1.start()
while False:
    print("Enter Command:")
    text = input()

    if text == "add floor":
        building.add_floor()

    elif text == "add room":
        print("which floor?")
        floor = input()
        print("room type (S/D/E): STANDARD, DELUXE, EXECUTIVE?S\nDELUXE ROOM IS FOR VIDEO CONFERENCING.\nEXECUTIVE ROOM IS FOR LIVE VIDEO CONFERENCING WITH RECORDING")
        room_type = input()
        print("Enter the Occupancy Capacity of the Hall:")
        occupancy = input()
        building.add_room(int(floor), room_type, occupancy)

    elif text == "detail":
        building.description()

    elif text == "add org":
        print("Fill the organisation's name:")
        org_name = input()
        print("Org's Contact:")
        contact = input()
        organisation.append(org(org_name, contact))

    elif text == "add user":
        print("Enter organisation:")
        org_name = input()
        if find(organisation, org_name):
            print("User Name:")
            user = input()
            print("email:")
            email = input()
            print("role:")
            role = input()
            print("Booking Permission Given (y/n):")
            bookingPermission = input()
            if bookingPermission == "y":
                bookingPermission = True
            else:
                bookingPermission = False
        else:
            print("Invalid Org.")
    
    elif text == "switch":
        print("Enter Org:")
        org_name = input()
        for i in organisation:
            if i.name == org_name:
                org = i
                break
        if org:
            print("User Name:")
            user = input()
            for i in org.user:
                if i.name == user:
                    user = i
                    break
            # IF USER NOT FOUND::
            print("Actions:")
            print("1. List all your bookings")
            print("2. List all your org bookings")
            print("3. Request Booking")
            print("Choose Action: (1/ 2/ 3):")
            action = input()
            # if else action
            if action == "3":
                print("Booking on which date:")
                print("Enter year")
                req = {}
                year = int(input())
                print("Enter month")
                month = int(input())
                print("Enter date")
                date = int(input())
                req["date"] = datetime.date(year, month, date)
                print(req["date"])
                if req["date"] < datetime.date.today():
                    print("Wrong Date.")
                    continue
                print("Choose room type (S/ D/ E):")
                req["type"] = input()
                print("Choose minimum occupancy:")
                occ = int(input())
                req["occupancy"] = occ
                print("Choose meeting start time:(0-23 hrs)")
                start = input()
                print("Choose end time:")
                end = input()
                available_slot = building.is_available(req, start, end)
                # for i in range(0, len(available_slot)):
                #     print(available_slot[i].description())
                


    elif text == "exit" or text == "e":
        break

# from floor import 1floor

# building = []

# building.append(floor())

# building[0].add_room({
#     "number": 1,
#     "room_type": "Executive",
# })

# print(building[0].total_room)

# print(len(building))

# building[0].is_available(0, "2023-09-02")