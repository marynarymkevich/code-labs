class Room:
    def __init__(self, room_number, type, max_number_of_persons):
        self.room_number = room_number
        self.type = type
        self.max_number_of_persons = max_number_of_persons
        self.is_available = True

    def __str__(self):
        return f"Room #{self.room_number}, {self.type} for maximum {self.max_number_of_persons} guests"

    def set_availability(self, isAvailable):
        self.is_available = isAvailable

    def get_availability(self):
        return self.is_available