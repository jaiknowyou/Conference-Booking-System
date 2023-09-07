from src.organisation import org
import threading
import datetime

# bookingSlot Class instances to save reservation related data
class bookingSlot:
    def __init__(self, id, userId, roomId, date, startTime, endTime):
        try:
            self.id = id
            self.roomId = roomId
            self.userId = userId
            self.date = date
            self.startTime = startTime
            self.endTime = endTime
            self.dateOfBooking = datetime.date.today()
            self.active = True
        except Exception as error:
            print("An error occurred in bookingSlot():", error)

# booingSystem links the building(Conference Rooms) and Org(Users) data to facilitate bookings
class bookingSystem:
    def __init__(self, title, location):
        try:
            self.title = title
            self.building = location
            self.organisation = []
            self.reservations = []    
            self.lockBooking = threading.Lock()
        except Exception as error:
            print("An error occurred in bookingSystem():", error)    

    def add_org(self, name, contact):
        try:
            self.organisation.append(org(self, len(self.organisation), name, contact))
            return self.organisation[-1]
        except Exception as error:
            print("An error occurred in bookingSystem.add_org():", error)

    def get_org(self, email):
        try:
            for ORG in self.organisation:
                if ORG.contact == email:
                    return ORG
            return None
        except Exception as error:
            print("An error occurred in bookingSystem.get_org():", error)

    def renew_monthly_limit(self):
        try:
            for ORG in self.organisation:
                ORG.renew_monthly_limit(30)
        except Exception as error:
            print("An error occurred in bookingSystem.renew_monthly_limit():", error)

    def generateId(self):
        try:
            return len(self.reservations)+1
        except Exception as error:
            print("An error occurred in bookingSystem.geberateId():", error)


    def add_booking(self, id, userId, roomId, date, startTime, endTime):
        try:
            Slot = bookingSlot(id, userId, roomId, date, startTime, endTime)
            self.reservations.append(Slot)
        except Exception as error:
            print("An error occurred in bookingSystem.add_booking():", error)

    def getDetail(self, bookingId):
        try:
            info = self.reservations[bookingId - 1]
            return info
        except Exception as error:
            print("An error occurred in bookingSystem.getDetail():", error)

    def changeStatus(self, bookingId):
        try:
            self.reservations[bookingId - 1].active = False
        except Exception as error:
            print("An error occurred in bookingSystem.changeStatus():", error)