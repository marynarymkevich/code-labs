from Models.booking import Booking
from data import rooms

bookings = []

def show_available_rooms():
    available_rooms = [room for room in rooms if room.get_availability()]
    
    if not available_rooms:
        print("Sorry, no rooms available at the moment.")
    else:
        print(f"\nOur available rooms:\n")
        for room in available_rooms:
            print(room)


def make_reservation(current_customer, selected_room_number, number_of_nights):
    for room in rooms:
        if room.room_number == selected_room_number:
            if room.get_availability():
                room.set_availability(False)
                bookings.append(Booking(room, current_customer, number_of_nights))
                print(f"\nGreat! Room {room.room_number} is now booked for you, {current_customer.firstname}")
            else:
                print("Sorry, this room is unavailable more")
            return
        
    print(f"No room with this number") 

def cancel_reservation(booking_index):
    if 0 <= booking_index < len(bookings):
        cancelled_booking = bookings.pop(booking_index)
        cancelled_booking.room.set_availability(True)
        print(f"\nBooking for Room #{cancelled_booking.room.room_number} successfully cancelled!")
        return True
    else:
        print(f"Please enter a number between 1 and {len(bookings)}.")
        return False

def show_customers_bookings():
    if bookings:
        for index, booking in enumerate(bookings, start=1):
            print(f"\n{index}. {booking}")
    else:
        print("You don't have bookings yet.")