# Part A - Conditions

# Task 1: Check number sign
value = float(input("Enter number: "))
if value > 0:
    print("Positive number")
elif value < 0:
    print("Negative number")
else:
    print("It is zero")


# Task 2: Age group classifier
user_age = int(input("How old are you? "))
if user_age < 13:
    print("Category: Child")
elif user_age < 18:
    print("Category: Teenager")
elif user_age < 60:
    print("Category: Adult")
else:
    print("Category: Senior")


# Task 3: Login check
SAVED_USER = "admin"
SAVED_PASS = "admin123"

input_user = input("Username: ")
input_pass = input("Password: ")

if input_user == SAVED_USER and input_pass == SAVED_PASS:
    print("Access granted!")
else:
    print("Invalid login or password.")


# Task 4: Student grade calculation
grade_score = int(input("Enter score (0-100): "))

if grade_score >= 90:
    print("Grade: A")
elif grade_score >= 80:
    print("Grade: B")
elif grade_score >= 70:
    print("Grade: C")
elif grade_score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Task 5: Calculate delivery cost
order_total = float(input("Total price: "))
is_member = input("Are you a member? (yes/no): ").strip().lower() == "yes"

if is_member or order_total >= 100:
    shipping_cost = 0
else:
    shipping_cost = 15

print(f"Shipping costs: ${shipping_cost}")


# Task 6: Five boolean expressions
print(18 == 20)  # False
print(45 != 12)  # True
print(8 > 3)     # True
print(14 < 9)    # False
print(25 >= 25)  # True


# Part B - Truthy, falsy and membership

# Task 1: Check values in if statements
examples = [
    "",          # empty string - falsy
    "python",    # non-empty string - truthy
    0,           # zero - falsy
    100,         # non-zero int - truthy
    [],          # empty list - falsy
    [10, 20]     # non-empty list - truthy
]

for val in examples:
    if val:
        print(f"Value '{val}' is truthy")
    else:
        print(f"Value '{val}' is falsy")


# Task 2: Language check
available_langs = ["english", "russian", "swedish", "german", "french"]

user_lang = input("Enter your language: ").strip().lower()

if user_lang in available_langs:
    print("Language is supported!")
else:
    print("Language not found.")


# Task 3: Blocked username
blocked_users = ["john", "anna", "banned_user", "alex"]

user_input = input("Choose a username: ").strip()

if user_input.lower() in blocked_users:
    print("Access denied.")
else:
    print(f"Welcome, {user_input}")


# Task 4: Readable conditions using not
temperature = 15
is_sunny = False
target_country = "Iceland"

if not (temperature > 20):
    print("Too cold for a beach vacation.")

if not (is_sunny and target_country == "Spain"):
    print("Choose another country for sunny weather.")



# Part C - For loops

# Task 1: Loop
people = ["Elena", "Marcus", "Sophia", "Oliver"]
for num, person in enumerate(people, 1):
    print(f"Member {num}: Welcome, {person}!")


# Task 2: Print even numbers 1-50
for val in range(1, 51):
    if val % 2 == 0:
        print(val)


# Task 3: List sum
expenses = [18, 55, 9, 10, 32, 6]
total = 0
for cost in expenses:
    total += cost
print(f"Total spent: ${total}")


# Task 4: Find maximum value
numbers = [12, 94, 63, 81, 47, 98, 23]
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print(f"Max: {max_value}")


# Task 5: Count long words (> 5 chars)
words = ["blueberry", "sky", "apartment", "run", "programming", "key"]
long_words_counter = 0
for text in words:
    if len(text) > 5:
        long_words_counter += 1
print(f"Total entries with 6+ characters: {long_words_counter}")


# Task 6: Pass fail threshold counter
scores = [91, 54, 78, 68, 88, 70, 61, 82]
successful_tests = 0
unsuccessful_tests = 0

for score in scores:
    if score >= 70:
        successful_tests += 1
    else:
        unsuccessful_tests += 1

print(f"Passed exams: {successful_tests}, Failed exams: {unsuccessful_tests}")


# Task 7: Iterate dictionary three ways
laptop_specs = {"brand": "Lenovo", "ram_gb": 16, "location": "Oslo"}

# Iterating over keys
for property_name in laptop_specs.keys():
    print(f"Attribute: {property_name}")

# Iterating over values
for property_val in laptop_specs.values():
    print(f"Value: {property_val}")

# Iterating over key-value pairs
for property_name, property_val in laptop_specs.items():
    print(f"{property_name} -> {property_val}")


# Part D - range, enumerate and nested loops

# Reverse loop from 10 to 1
for x in range(10, 0, -1):
    print(x)


# Multiplication table for user input
user_num = int(input("Provide a number: "))
for multiplier in range(1, 11):
    print(f"{user_num} * {multiplier} = {user_num * multiplier}")


# Playlist
my_favorites = ["Blinding Lights", "Shape of You", "Levitating", "As It Was"]
for track_idx, track_name in enumerate(my_favorites, start=1):
    print(f"Song #{track_idx} - {track_name}")


# Nested loops
for x in range(1, 4):
    for y in range(1, 5):
        print(f"Point ({x}, {y})")


# 5x5 text grid
for r in range(5):
    for c in range(5):
        print("X", end=" ")
    print()  # new line after each row


# Part E - While loops

# Countdown 10 to 0
countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1


# Password check
correct_password = "qwe123"
password = ""

while password != correct_password:
    password = input("Enter password: ").strip()
    if password != correct_password:
        print("Wrong password, try again.")

print("Access granted!")


# Interactive menu until 'quit'
option = ""
while option != "quit":
    option = input("Choose option (play / info / quit): ").strip().lower()
    if option != "quit":
        print(f"Selected option: {option}")

print("Goodbye!")


# Accumulate sum until 0
running_total = 0
while True:
    number = float(input("Enter number (0 to stop): "))
    if number == 0:
        break
    running_total += number

print(f"Running total: {running_total}")


# Number guess
secret_number = 85
guess = None

while guess != secret_number:
    guess = int(input("Enter guess: "))
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("You guessed it!")


# Part F - break and continue

# First number divisible by both 7 and 9
for number in range(1, 101):
    if number % 7 == 0 and number % 9 == 0:
        print(f"First match: {number}")
        break


# # Skip empty strings
strings = ["apple", "", "banana", "", "cherry", "date"]
for string in strings:
    if string == "":
        continue
    print(f"Current string: {string}")


# # Search for a target name
names = ["Sophia", "Liam", "Emma", "Noah"]
target_name = "Emma"
found = False

for name in names:
    if name == target_name:
        print("found")
        found = True
        break

# We know it was not found because the loop completed without triggering the break and setting found to True
if not found:
    print("The name was not found")


# Process numeric values, skip negative values, stop at 999
numeric_values = [42, -5, 18, -12, 87, 999, 100, -3]
for value in numeric_values:
    if value == 999:
        print("Stop process completely.")
        break
    if value < 0:
        continue
    print(f"Value: {value}")


# Part G
# List of dictionaries
sessions = [
    {"subject": "Python", "minutes": 10},
    {"subject": "Math", "minutes": 20},
    {"subject": "Python", "minutes": 30},
    {"subject": "Web", "minutes": 40},
    {"subject": "Math", "minutes": 10},
    {"subject": "Python", "minutes": 20},
    {"subject": "Web", "minutes": 30},
    {"subject": "Database", "minutes": 75},
    {"subject": "Math", "minutes": 75},
    {"subject": "Python", "minutes": 55}
]


# # Total minutes
total_minutes = 0
for session in sessions:
    total_minutes += session["minutes"]
print("total_minutes: ", total_minutes)


# Total minutes with empty dictionary
subject_totals = {}
for session in sessions:
    subject = session["subject"]
    subject_minutes = session["minutes"]
    if subject in subject_totals:
        subject_totals[subject] += subject_minutes
    else:
        subject_totals[subject] = subject_minutes
print(f"Total minutes per subject: {subject_totals}")



# # 4. Longest session
longest_session = sessions[0]
for session in sessions:
    if session["minutes"] > longest_session["minutes"]:
        longest_session = session
print(f"Longest session: {longest_session['subject']} - {longest_session['minutes']} min")


# # Sessions longer than 45 minutes
print("\nSessions longer than 45 minutes:")
for session in sessions:
    if session["minutes"] <= 45:
        continue  
    print(f"{session['subject']}: {session['minutes']} min")


# Repeated menu with break/continue
while True:
    print("MENU")
    print("1. View all sessions")
    print("2. View total time")
    print("3. Filter by subject")
    print("4. Quit")
    
    choice = input("Select an option (1-4): ").strip()

    if choice == "4":
        print("Quit")
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid, try again.")
        continue

    if choice == "1":
        for session in sessions:
            print(f"{session['subject']}: {session['minutes']} minutes")
    elif choice == "2":
        print(f"Total time studied: {total_minutes} minutes")
    elif choice == "3":
        filter_sub = input(f"Enter subject {list(subject_totals.keys())}: ").strip()
        found = False
        for session in sessions:
            if session["subject"].lower() == filter_sub.lower():
                print(f"- {session['subject']}: {session['minutes']} minutes")
                found = True
        if not found:
            print("No sessions found for this subject.")


# Part H

# FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Count vowels
sentence = "Python Programming Task"
vowels = "aeiouAEIOU"
vowels_count = 0

for char in sentence:
    if char in vowels:
        vowels_count += 1

print(f"Total vowels: {vowels_count}")


# Find duplicates
items = ["apple", "banana", "apple", "cherry", "banana", "date", "apple"]
existed = set()
duplicates = set()

for item in items:
    if item in existed:
        duplicates.add(item)
    else:
        existed.add(item)

print(f"Duplicates: {list(duplicates)}")


# Text histogram
numbers = [3, 5, 2]

for num in numbers:
    print("*" * num)
