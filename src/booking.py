# data required = building , user, date and time slot - user requirement and slot filter
from organisation import org
import threading
    
class bookingSlot:
    def __init__(self, id, userId, roomId, date, startTime, endTime):
        self.id = id
        self.roomId = roomId
        self.userId = userId
        self.date = date
        self.startTime = startTime
        self.endTime = endTime
        self.active = True

class bookingSystem:
    def __init__(self, title):
        self.title = title
        self.organisation = []
        self.reservations = []    
        self.lockBooking = threading.Lock()    

    def add_org(self, name, contact):
        self.organisation.append(org(len(self.organisation), name, contact))

    def get_org(self, email):
        for ORG in self.organisation:
            if ORG.contact == email:
                return ORG
        return None

    def renew_monthly_limit(self):
        for ORG in self.organisation:
            ORG.renew_monthly_limit(30)

    def generateId(self):
        return len(self.reservations)+1


    def add_booking(self, id, userId, roomId, date, startTime, endTime):
        Slot = bookingSlot(id, userId, roomId, date, startTime, endTime)
        self.reservations.append(Slot)