from constants import DATE_FORMAT
from datetime import date, datetime

def get_valid_positive_int(prompt, error_message="Please enter a valid number."):
    while True:
        try:
            user_number = int(input(prompt))
            if user_number > 0:
                return user_number
            print("Number must be greater than 0.")
        except ValueError:
            print(error_message)

def get_valid_text(prompt, error_message="Input cannot be empty. Please try again."):
    while True:
        user_text = input(prompt).strip()
        if user_text:
            return user_text
        print(error_message)

def get_valid_date(prompt, error_message="Please enter a valid date format."):
    while True:
        user_date = input(prompt).strip()
        try:
            parsed_date = datetime.strptime(user_date, DATE_FORMAT).date()
            if parsed_date >= date.today():
                return parsed_date
            print("Date cannot be in the past.")
            continue
        except ValueError:
            print(error_message)
            continue

        
