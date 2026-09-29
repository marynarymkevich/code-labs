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
available_rooms = None

def display_menu():
    print("\n\n" + "="*30)
    print(" BOOKING SYSTEM MENU ")
    print("="*30)
    print("1. View available rooms")
    print("2. Book a room")
    print("3. View my bookings")
    print("4. Cancel a booking")
    print("5. Exit")
    print("="*30)

def show_available_rooms():
    available_rooms = [room for room in rooms if room.get_availability()]
    
    if not available_rooms:
        print("Sorry, no rooms available at the moment.")
    else:
        print(f"\nOur available rooms:\n")
        for room in available_rooms:
            print(room)

def get_customer():
    print(f"\nTo make a reservation we need to know your name")

    customer_first_name = input("Please enter your first name: ")
    customer_last_name = input("Please enter your last name: ")
    print(f"Nice to see you, {customer_first_name} {customer_last_name}")

    return Customer(customer_first_name, customer_last_name)

def get_room_number():
    while True:
        try:
            return int(input("Enter room number to reserve: "))
        except ValueError:
            print("Please enter a valid room number.")

def get_number_of_nights():
    while True:
        try:
            nights = int(input("Enter how many nights you need: "))
            if nights > 0:
                return nights
            print("Number of nights must be at least 1.")
        except ValueError:
            print("Please enter a valid number of nights.")

def show_customers_bookings():
    if bookings:
        for index, booking in enumerate(bookings, start=1):
            print(f"{index}. {booking}")
    else:
        print("You don't have bookings yet.")

# Main menu
while True:
    display_menu()
    choice = input(f"Please enter a number of the action for you (1-4): \n\n\n")

    if choice == "1":
        show_available_rooms()

    elif choice == "2":
        if current_customer is None:
            current_customer = get_customer()

        selected_room_number = get_room_number()
        number_of_nights = get_number_of_nights()
        for room in rooms:
            if room.room_number == selected_room_number:
                if room.get_availability():
                    room.set_availability(False)
                    bookings.append(Booking(room, current_customer, number_of_nights))
                    print(f"\nGreat! Room {room.room_number} is now booked for you, {current_customer.firstname}")
                else:
                    print("Sorry, this room is unavailable more")
                break
        else:
            print(f"No room with this number") 
    elif choice == "3":
        show_customers_bookings()
    elif choice == "4":
        show_customers_bookings()
        booking_number = input("Please enter the number of booking you want to cancel: ")
        room_number_for_canceling = bookings[room_number_for_canceling].room.room_number 
        bookings[booking_number].remove()
        for room in rooms:
            if room.room_number == room_number_for_canceling:
                room.set_availability(True)
                
    elif choice == "5":
        print("\nThank you for using our Booking System. Bye!")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")










   