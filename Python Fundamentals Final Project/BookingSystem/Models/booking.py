from datetime import date, timedelta

class Booking: 
    def __init__(self, room, customer, date_of_start, nights):
        self.room = room
        self.customer = customer
        self.date_of_start = date_of_start
        self.nights = nights
        self.end_date = self.calculate_date_of_end()
        self.total_price = self.room.price_per_night * self.nights
        self.total_price = self.calculate_total_price()

    def __str__(self):
        return f"{self.room} | from {self.date_of_start} till {self.end_date} | {self.nights} nights | Guest: {self.customer} | Total: {self.total_price}"

    def calculate_total_price(self):
        return self.room.price_per_night * self.nights

    def calculate_date_of_end(self):
        return (self.date_of_start + timedelta(days=self.nights)).strftime("%Y-%m-%d")

    def get_receipt(self):
        return (
            f"\n--- RECEIPT ---"
            f"\nGuest: {self.customer}"
            f"\nRoom: #{self.room.room_number}"
            f"\nFrom: {self.date_of_start}"
            f"\nTill: {self.end_date}"
            f"\nNights: {self.nights}"
            f"\nTotal: ${self.total_price}"
            f"\n---------------"
        )

    
    