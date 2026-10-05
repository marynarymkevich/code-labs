from datetime import date, timedelta
from constants import DATE_FORMAT

class Booking: 
    def __init__(self, room, customer, date_of_start, nights):
        self.room = room
        self.customer = customer
        self.date_of_start = date_of_start # Object
        self.nights = nights
        self.end_date = self.calculate_date_of_end() #Object
        self.total_price = self.calculate_total_price()

    def __str__(self):
        formatted_start_date = self.date_of_start.strftime(DATE_FORMAT)
        formatted_end_date = self.end_date.strftime(DATE_FORMAT)
        
        return f"{self.room} | from {formatted_start_date} till {formatted_end_date} | {self.nights} nights | Guest: {self.customer} | Total: {self.total_price}"

    def calculate_total_price(self):
        return self.room.price_per_night * self.nights

    def calculate_date_of_end(self):
        return (self.date_of_start + timedelta(days=self.nights))

    def get_receipt(self):
        formatted_start_date = self.date_of_start.strftime(DATE_FORMAT)
        formatted_end_date = self.end_date.strftime(DATE_FORMAT)

        return (
            f"\n--- RECEIPT ---"
            f"\nGuest: {self.customer}"
            f"\nRoom: #{self.room.room_number}"
            f"\nFrom: {formatted_start_date}"
            f"\nTill: {formatted_end_date}"
            f"\nNights: {self.nights}"
            f"\nTotal: ${self.total_price}"
            f"\n---------------"
        )

    
    