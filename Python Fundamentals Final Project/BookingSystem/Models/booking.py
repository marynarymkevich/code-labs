class Booking: 
    def __init__(self, room, customer, nights):
        self.room = room
        self.customer = customer
        self.nights = nights
        self.total_price = self.room.price_per_night * self.nights
        self.total_price = self.calculate_total_price()

    def __str__(self):
            return f"{self.room} | {self.nights} nights | Total: {self.total_price} | Guest: {self.customer}"

    def calculate_total_price(self):
        return self.room.price_per_night * self.nights

    def get_receipt(self):
        return (
            f"\n--- RECEIPT ---"
            f"\nGuest: {self.customer}"
            f"\nRoom: #{self.room.room_number}"
            f"\nNights: {self.nights}"
            f"\nTotal: ${self.total_price}"
            f"\n---------------"
        )

    
    