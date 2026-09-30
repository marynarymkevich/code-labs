from models.customer import Customer
from booking_services import bookings, show_available_rooms, make_reservation, cancel_reservation, show_customers_bookings

current_customer = None

def display_menu():
    print("\n\n" + "="*30)
    print(" BOOKING SYSTEM MENU ")
    print("="*30)
    print("1. View available rooms")
    print("2. Search rooms by filters")
    print("3. Book a room")
    print("4. View my bookings")
    print("5. Cancel a booking")
    print("6. Exit")
    print("="*30)

def get_customer():
    print(f"\nTo make a reservation we need to know your name")

    customer_first_name = input("Please enter your first name: ")
    customer_last_name = input("Please enter your last name: ")
    print(f"Nice to see you, {customer_first_name} {customer_last_name}")

    return Customer(customer_first_name, customer_last_name)

def search_rooms_menu():
    print("\nSearch rooms")
    print("1. Search by number of guests")
    print("2. Search by maximum price")
    print("3. View VIP rooms only")
    
    search_choice = input("Select search option (1-3): ").strip()
    
    if search_choice == "1":
        try:
            persons = int(input("How many guests? "))
        except ValueError:
            print("Please enter a valid number.")
            
    elif search_choice == "2":
        pass
            
    elif search_choice == "3":
        pass

def show_results(found_rooms):
    if not found_rooms:
        print("\nNo matching rooms found.")
    else:
        print(f"\nFound {len(found_rooms)} room(s):\n")
        for room in found_rooms:
            print(room)

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


# Main menu
while True:
    display_menu()
    choice = input(f"Please enter a number of the action for you (1-6): \n\n\n")

    if choice == "1":
        show_available_rooms()

    if choice == "2":
            show_available_rooms()

    elif choice == "3":
        if current_customer is None:
            current_customer = get_customer()

        selected_room_number = get_room_number()
        number_of_nights = get_number_of_nights()

        make_reservation(current_customer, selected_room_number, number_of_nights)

    elif choice == "4":
        show_customers_bookings()

    elif choice == "5":
        if not bookings:
            print("\nYou don't have active bookings to cancel.")
        else:
            show_customers_bookings()
            while True:
                try:
                    user_input = int(input("\nPlease enter the number of booking you want to cancel: "))
                    if cancel_reservation(user_input):
                        break
                except ValueError:
                    print("Please enter a valid number.")

    elif choice == "6":
        print("\nThank you for using our Booking System. Bye!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 6.")










   