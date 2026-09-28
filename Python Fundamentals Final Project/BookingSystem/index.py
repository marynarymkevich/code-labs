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
current_customer = None
selected_room_number = None
number_of_nights = None
available_rooms = [room for room in rooms if room.get_availability()]

print(f"\n***Welcome! Below you can see all our available rooms.***\n")
for room in available_rooms:
    print(f"{room}")

def get_customer():
    print(f"\nTo make a reservation we need to know your name")

    customer_first_name = input("Please enter your first name: ")
    customer_last_name = input("Please enter your last name: ")
    print(f"Nice to see you, {customer_first_name} {customer_last_name}")

    return Customer(customer_first_name, customer_last_name)

current_customer = get_customer()

def get_room_number():
    while True:
        try:
            return int(input("Enter room number to reserve: "))
        except ValueError:
            print("Please enter a valid room number.")

selected_room_number = get_room_number()

def get_number_of_nights():
    while True:
        try:
            nights = int(input("Enter how many nights you need: "))
            if nights > 0:
                return nights
            print("Number of nights must be at least 1.")
        except ValueError:
            print("Please enter a valid number of nights.")

number_of_nights = get_number_of_nights()

for room in rooms:
    if room.room_number == selected_room_number:
        if room.get_availability():
            room.set_availability(False)
            bookings.append(Booking(room, current_customer, number_of_nights))
            print(f"Great! Room {room.room_number} is now booked for you, {current_customer.firstname}")
        else:
            print("Sorry, this room is unavailable more")
        break
else:
    print(f"No room with this number")    