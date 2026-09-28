class Room:
    def __init__(self, room_number, type, max_number_of_persons):
        self.room_number = room_number
        self.type = type
        self.max_number_of_persons = max_number_of_persons

    def setAvailability(self, isAvailable):
        self.isAvailable = isAvailable

    def getAvailability(self):
        return self.isAvailable