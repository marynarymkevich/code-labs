class Room:
    def __init__(self, room_number, room_type, price_per_night, max_number_of_persons=2):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.max_number_of_persons = max_number_of_persons
        self.is_available = True

    def __str__(self):
        return f"Room #{self.room_number} ({self.room_type}) - ${self.price_per_night}/night"

    def set_availability(self, is_available):
        self.is_available = is_available

    def get_availability(self):
        return self.is_available


class VIP_Room(Room):
    def __init__(self, room_number, price_per_night, max_number_of_persons=4, has_free_breakfast=True):
        super().__init__(room_number, "VIP", price_per_night, max_number_of_persons)
        self.has_free_breakfast = has_free_breakfast

    def __str__(self):
        base_info = super().__str__()
        breakfast_info = " | Free Breakfast Included" if self.has_free_breakfast else ""
        return f"[VIP] {base_info}{breakfast_info}"