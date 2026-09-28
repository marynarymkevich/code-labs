from Models.room import Room
from Models.customer import Customer
from Models.booking import Booking

rooms = [
    Room(101, "Single", 1),
    Room(102, "Single", 1),
    Room(103, "Double", 2),
    Room(104, "Double", 2),
    Room(201, "Suite", 3),
    Room(202, "Family Suite", 4),
    Room(203, "Penthouse", 5)
]

bookings = []

available_rooms = [room for room in rooms if room.get_availability()]

print(f"\n***Welcome! Below you can see all our available rooms.***\n")
for room in available_rooms:
    print(f"{room}")

print(f"\nTo make a reservation we need to know your name")
customer_first_name = input("Please enter your first name: ")
customer_last_name = input("Please enter your last name: ")
print(f"Nice to see you, {customer_first_name} {customer_last_name}")
current_customer = Customer(customer_first_name, customer_last_name)

selected_number = int(input("Enter room number to reserve: "))
number_of_nights = int(input("Enter how many nights you need: "))

for room in rooms:
    if room.room_number == selected_number:
        if room.get_availability():
            room.set_availability(False)
            bookings.append(Booking(room, current_customer, number_of_nights))
            print(f"Great! Room {room.room_number} is now booked for you, {customer_first_name}")
        else:
            print("Sorry, this room is unavailable more")
        break