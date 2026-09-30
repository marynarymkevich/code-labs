class Booking: 
    def __init__(self, room, customer, nights):
        self.room = room
        self.customer = customer
        self.nights = nights
        self.total_price = self.room.price_per_night * self.nights

    def __str__(self):
        return f"{self.room} | {self.nights} nights | Total: {self.total_price} | Guest: {self.customer}"

    