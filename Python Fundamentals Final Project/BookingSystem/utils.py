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
