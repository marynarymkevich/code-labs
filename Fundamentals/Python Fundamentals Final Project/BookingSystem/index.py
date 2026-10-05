from models.customer import Customer
from booking_services import (
    bookings, 
    show_available_rooms, 
    make_reservation, 
    cancel_reservation, 
    show_customers_bookings, 
    show_search_results, 
    find_rooms_by_capacity, 
    find_rooms_by_price, 
    find_rooms_by_type
)
from utils import get_valid_text, get_valid_positive_int, get_valid_date
from constants import DATE_FORMAT_DISPLAY

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

    customer_first_name = get_valid_text("Please enter your first name: ")
    customer_last_name = get_valid_text("Please enter your last name: ")
    print(f"\nNice to see you, {customer_first_name} {customer_last_name}!\n")

    return Customer(customer_first_name, customer_last_name)

def search_rooms_menu():
    while True:
        print("\n" + "="*15)
        print("Search rooms")
        print("="*15)
        print("1. Search by number of guests")
        print("2. Search by maximum price")
        print("3. View VIP rooms only")
        print("4. Exit from rooms search")
        
        search_choice = input("Select search option (1-4): ").strip()
        
        if search_choice == "1":
            persons = get_valid_positive_int("How many guests? ", "Enter a valid number of guests")   
            results = find_rooms_by_capacity(persons)
            show_search_results(results)    
        elif search_choice == "2":
            customer_price = get_valid_positive_int("What the maximum price ($) per night (min 50$)?", "Enter valid price")
            results = find_rooms_by_price(customer_price)
            show_search_results(results) 
        elif search_choice == "3":
            results = find_rooms_by_type("VIP")
            show_search_results(results)
        elif search_choice == "4":
            break
        else:
            print("\nNo such option. Please select search option (1-4)")

def get_room_number():
    return get_valid_positive_int("Enter room number to reserve: ", "Please enter a valid room number.")

def get_number_of_nights():
    return get_valid_positive_int("Enter how many nights you need: ", "Please enter a valid number of nights.")

def get_date_of_start():
    return get_valid_date(f"Enter the start day in format {DATE_FORMAT_DISPLAY}: ", f"The date should be in format {DATE_FORMAT_DISPLAY}")

# Main menu
def main():
    global current_customer

    while True:
        display_menu()
        choice = input(f"Please enter a number of the action for you (1-6): \n").strip()

        if choice == "1":
            show_available_rooms()

        elif choice == "2":
            search_rooms_menu()

        elif choice == "3":
            if current_customer is None:
                current_customer = get_customer()

            selected_room_number = get_room_number() # TODO change the order, ask date and nights, show availaable, them ask room number/check it
            number_of_nights = get_number_of_nights()
            date_of_start = get_date_of_start()

            make_reservation(
                current_customer, 
                selected_room_number, 
                date_of_start, 
                number_of_nights
            )

        elif choice == "4":
            show_customers_bookings()

        elif choice == "5":
            if not bookings:
                print("\nYou don't have active bookings to cancel.")
            else:
                show_customers_bookings()
                while True:
                    user_input = get_valid_positive_int("\nPlease enter the number of booking you want to cancel: ")
                    if cancel_reservation(user_input):
                        break

        elif choice == "6":
            print("\nThank you for using our Booking System. Bye!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 6.")

main()








   