import datetime
import time
from src.building import building
from src.booking import bookingSystem
from src.testCases import testCase

# initialising Conference Building with number of Floor as parameter
building = building(3)
building.add_floor()

# initialising Booking system
# All operations and information would be available through this Object
booking = bookingSystem("VARAHA CONFERENCE OFFICES", building)

# To run test cases
print("For running test cases: Type t")
print("else type e for exit")
text = input()
while text == "t":
    t = testCase(booking)
    while True:
        i = 1
        if i == 1:
            t.testCase1()
            text = input()
            i += 1
        if i == 2:
            t.testCase2()
            text = input()
            i += 1
        if i == 3:
            t.testCase3()
            text = input()
            i += 1
        if i == 4:
            t.testCase4()
            text = input()
            i += 1
        if i == 5:
            t.testCase5()
            text = input()
            i += 1
        if i == 6:
            t.testCase6()
            text = input()
            i += 1
        if i == 7:
            t.testCase7()
            text = input()
            i += 1
        if i == 8:
            t.testCase8()
            text = input()
            i += 1
        if i == 9:
            t.testCase9()
            text = input()
            i += 1
        if i == 10:
            t.testCase10()
            text = input()
            i += 1
        if i == 11:
            t.testCase11()
            text = input()
            i += 1
        if i == 12:
            t.testCase12()
            print("To run testCase13 now, type 13")
            text = input()
        if text == "13":
            t.testCase13()
            text = input()
            text = "e"
        if text == "e":
            break
    break


# initialising Conference Rooms
print("All test Cases Complete.")
print("\n")

time.sleep(1)

building.add_room(0, "S", 9)
building.add_room(4, "D", 6)
building.add_room(1, "E", 8)
building.description()

# Monthly booking limit Renews at the first day of the month == 30
if datetime.date.today().day == 1:
    booking.renew_monthly_limit()

# For Command Line (Manual Booking):
# while True:
#     print("Enter Command:")
#     text = input()

#     if text == "add floor":
#         building.add_floor()

#     elif text == "add room":
#         print("which floor?")
#         floor = input()
#         print("room type (S/D/E): STANDARD, DELUXE, EXECUTIVE?S\nDELUXE ROOM IS FOR VIDEO CONFERENCING.\nEXECUTIVE ROOM IS FOR LIVE VIDEO CONFERENCING WITH RECORDING")
#         room_type = input()
#         print("Enter the Occupancy Capacity of the Hall:")
#         occupancy = input()
#         building.add_room(int(floor), room_type, occupancy)

#     elif text == "detail":
#         building.description()

#     elif text == "add org":
#         print("Fill the organisation's name:")
#         org_name = input()
#         print("Org's Contact:")
#         contact = input()
#         organisation.append(org(org_name, contact))

#     elif text == "add user":
#         print("Enter organisation:")
#         org_name = input()
#         if find(organisation, org_name):
#             print("User Name:")
#             user = input()
#             print("email:")
#             email = input()
#             print("role:")
#             role = input()
#             print("Booking Permission Given (y/n):")
#             bookingPermission = input()
#             if bookingPermission == "y":
#                 bookingPermission = True
#             else:
#                 bookingPermission = False
#         else:
#             print("Invalid Org.")
    
#     elif text == "switch":
#         print("Enter Org:")
#         org_name = input()
#         for i in organisation:
#             if i.name == org_name:
#                 org = i
#                 break
#         if org:
#             print("User Name:")
#             user = input()
#             for i in org.user:
#                 if i.name == user:
#                     user = i
#                     break
#             # IF USER NOT FOUND::
#             print("Actions:")
#             print("1. List all your bookings")
#             print("2. List all your org bookings")
#             print("3. Request Booking")
#             print("Choose Action: (1/ 2/ 3):")
#             action = input()
#             # if else action
#             if action == "3":
#                 print("Booking on which date:")
#                 print("Enter year")
#                 req = {}
#                 year = int(input())
#                 print("Enter month")
#                 month = int(input())
#                 print("Enter date")
#                 date = int(input())
#                 req["date"] = datetime.date(year, month, date)
#                 print(req["date"])
#                 if req["date"] < datetime.date.today():
#                     print("Wrong Date.")
#                     continue
#                 print("Choose room type (S/ D/ E):")
#                 req["type"] = input()
#                 print("Choose minimum occupancy:")
#                 occ = int(input())
#                 req["occupancy"] = occ
#                 print("Choose meeting start time:(0-23 hrs)")
#                 start = input()
#                 print("Choose end time:")
#                 end = input()
#                 available_slot = building.is_available(req, start, end)
#                 for i in range(0, len(available_slot)):
#                     print(available_slot[i].description())
#     elif text == "exit" or text == "e":
#         break