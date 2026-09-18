# ========== Part A - Function fundamentals ============

# # 1. Basic functions
# def greet():
#     print("Hello! Welcome to Python.")

def show_course_name():
    print("Course: Python Programming")

def print_separator():
    print("-" * 30)


# 2. Functions with parameters
def greet_person(name):
    print(f"Hello, {name}!")

def introduce(name, city):
    print(f"{name} is from {city}.")


# 3. Basic math operations returning values
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b


# 4. Parameter vs Argument example:
# 'width' and 'height' are parameters
# 5 and 4 are arguments
def calculate_area(width, height):
    return width * height


# 5. Use returned value in another calculation
room_area = calculate_area(5, 4)
total_paint_cost = room_area * 15



# ========== Part B - Return values ============

# 1. Write is_even(number)
def is_even(number):
    return number % 2 == 0


# 2. Write get_larger(a, b)
def get_larger(a, b):
    if a > b:
        return a
    return b


# 3. Write classify_score(score)
def classify_score(score):
    if score >= 50:
        return "PASS"
    return "FAIL"


# 4. Write full_name(first_name, last_name)
def full_name(first_name, last_name):
    return f"{first_name.strip().title()} {last_name.strip().title()}"


# 5. Write calculate_discount(price, percent)
def calculate_discount(price, percent):
    discount_amount = price * (percent / 100)
    return price - discount_amount


# 6. Example why print(result) inside a function is not the same as return result.
def print_inside(a, b):
    print(a + b)

def return_inside(a, b):
    return a + b



# ========= Part C =========================

# 1. Greet function
def greet(name, greeting='Hello'):
    return f"{greeting}, {name}!"


# 2. Calculate_price function
def calculate_price(price, quantity=1, discount=0):
    total = price * quantity
    final_total = total - discount
    return final_total


# 3. Create_profile function
def create_profile(name, city='Unknown', active=True):
    return {
        'name': name,
        'city': city,
        'active': active
    }


# 5. Invalid default-parameter ordering example:
# SyntaxError: non-default argument follows default argument
# def invalid_function(city='Unknown', name):
#     return f"{name} lives in {city}"
# Explanation: Parameters with default values must always come AFTER parameters without default values.



# ======== Part D - Functions and collections ==============

# 1. Write calculate_total(numbers) manually using a loop
def calculate_total(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# 2. Write count_even(numbers)
def count_even(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count


# 3. Write get_long_words(words, minimum_length) returning a new list
def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) >= minimum_length:
            long_words.append(word)
    return long_words


# 4. Write find_student(students, name) returning dictionary or None
def find_student(students, name):
    for student in students:
        if student['name'].lower() == name.lower():
            return student
    return None


# 5. Write average_score(students) for a list of dictionaries containing score values
def average_score(students):
    if not students:
        return 0.0
    
    total_score = 0
    for student in students:
        total_score += student['score']
    return total_score / len(students)


# 6. Write get_active_users(users) returning only dictionaries where active is True
def get_active_users(users):
    active_users = []
    for user in users:
        if user.get('active') is True:
            active_users.append(user)
    return active_users



# ==== Part E - Decomposition ===========================================

# 1. Temperature report
def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def classify_temperature(fahrenheit):
    if fahrenheit >= 85:
        return 'hot'
    elif fahrenheit >= 60:
        return 'warm'
    else:
        return 'cold'

def format_report(celsius):
    temp_fahrenheit = celsius_to_fahrenheit(celsius)
    classification = classify_temperature(temp_fahrenheit)

    return f"Today is {temp_fahrenheit:.1f}°F. It is {classification}."


# 2. Order calculation
order = {
    'salad': 250,
    'fish': 350,
    'coffee': 50,
    'dessert': 80
}

def get_subtotal(order):
    subtotal = 0
    for price in order.values():
        subtotal += price
    return subtotal

def get_with_discount(summ):
    if summ >= 200:
        return summ * 0.8
    elif summ >= 100:
        return summ * 0.9
    else:
        return summ

def get_final_total(order):
    return get_with_discount(get_subtotal(order))


# 3. Refactor
def get_passing_scores(scores):
    passing = []
    for score in scores:
        if score >= 60:
            passing.append(score)
    return passing

def sum_scores(scores):
    total = 0
    for score in scores:
        total += score
    return total

def calculate_passing_average(scores):
    passing = get_passing_scores(scores)
    if not passing:
        return 0.0
    return sum_scores(passing) / len(passing)



# ========= Part F - Applied challenge: Event registration processor ===================

# 1. Normalize
def normalize_name(name):
    return name.strip().title()

def validate_age_range(age: int) -> bool:

    return 18 <= age <= 80

def calculate_registration_fee(age: int, is_student: bool) -> int:
    if is_student:
        return 50
    elif age >= 65:
        return 60
    else:
        return 100

def create_participant_dictionary(name, age, is_student):
    if not validate_age_range(age):
        return None

    normalized_name = normalize_name(name)
    registration_fee = calculate_registration_fee(age, is_student)

    return {
        'name': normalized_name,
        'age': age,
        'is_student': is_student,
        'registration_fee': registration_fee
    }


# 2. Create 8 participant dictionaries
participant_list = [
    create_participant_dictionary("  john doe ", 22, True),
    create_participant_dictionary("jane smith", 30, False),
    create_participant_dictionary("ALICE JOHNSON", 19, True),
    create_participant_dictionary("bob brown", 68, False),
    create_participant_dictionary("charlie davis", 25, True),
    create_participant_dictionary("  EMMA WILSON", 45, False),
    create_participant_dictionary("fiona clark", 21, True),
    create_participant_dictionary("george harris", 72, False)
]


# 3. Expected registration revenue
def calculate_total_revenue(participant_list):
    total_revenue = 0
    for participant in participant_list:
        total_revenue += participant['registration_fee']
    return total_revenue


# 4. Write a function that returns only student participants
def get_student_participants(participant_list):
    students = []
    for participant in participant_list:
        if participant['is_student']:
            students.append(participant)
    return students


# 5. Write a function that returns the oldest participant
def get_oldest_participant(participant_list):
    if not participant_list:
        return None

    oldest_participant = participant_list[0]
    for participant in participant_list:
        if participant['age'] > oldest_participant['age']:
            oldest_participant = participant
            
    return oldest_participant


# 6. Readable summary string for one participant
def create_participant_summary(participant):
    student_status = "Student" if participant['is_student'] else "Non-Student"
    return f"Name: {participant['name']} | Age: {participant['age']} | Status: {student_status} | Fee: ${participant['registration_fee']}"


# =========== Part G - Strech challenges ================
# 1. Minimum and maximum
def get_min_and_max(numbers: list) -> tuple:
    """Returns min and max from list without min()/max()."""
    if not numbers:
        return None, None

    min_val = numbers[0]
    max_val = numbers[0]

    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    return min_val, max_val


# 2. Is palindrome
def is_palindrome(word: str) -> bool:
    """Checks if a given word or string is a palindrome."""
    cleaned = str(word).lower().replace(" ", "")
    return cleaned == cleaned[::-1]


# 3. Chart count
def count_character_frequencies(text: str) -> dict:
    """Counts the frequency of each character in a string."""
    frequencies = {}
    for char in text:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


# Count 
def count_number_types(numbers: list) -> dict:
    """Counts positive, negative and zero in list."""
    counts = {
        'positive': 0,
        'negative': 0,
        'zero': 0
    }
    for num in numbers:
        if num > 0:
            counts['positive'] += 1
        elif num < 0:
            counts['negative'] += 1
        else:
            counts['zero'] += 1
    return counts















# ==========================================
# Main execution section
def main():

    print("--- Part A: Task 1 (Basic functions) ---")
    show_course_name()
    print_separator()
    print_separator()

    print("\n--- Task 2 (Parameters) ---")
    greet_person("Alice")
    introduce("Bob", "London")

    print("\n--- Task 3 (Arithmetic) ---")
    print(f"Add 10 + 5: {add(10, 5)}")
    print(f"Subtract 10 - 5: {subtract(10, 5)}")
    print(f"Multiply 10 * 5: {multiply(10, 5)}")
    print(f"Divide 10 / 5: {divide(10, 5)}")

    print("\n--- Task 5 (Calculate Area) ---")
    print(f"Room area: {room_area}")
    print(f"Total paint cost: ${total_paint_cost}\n")


    print("\n--- Part B: Task 1 (is_even) ---")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Is 7 even? {is_even(7)}\n")

    print("--- Task 2 (get_larger) ---")
    print(f"Larger between 12 and 25: {get_larger(12, 25)}\n")

    print("--- Task 3 (classify_score) ---")
    print(f"Score 75: {classify_score(75)}")
    print(f"Score 42: {classify_score(42)}\n")

    print("--- Task 4 (full_name) ---")
    print(f"Formatted name: {full_name('john', 'doe')}\n")

    print("--- Task 5 (calculate_discount) ---")
    print(f"Price $100 with 20% discount: ${calculate_discount(100, 20)}\n")

    print("--- Task 6 (print vs return) ---")
    val1 = print_inside(5, 5)  
    val2 = return_inside(5, 5)
    print(f"Value from print function: {val1}")   # None
    print(f"Value from return function: {val2}")  # 10


    print("\n\n--- Part C: Task 1 (greet) ---")
    print(greet("Alice"))                  
    print(greet("Bob", greeting="Welcome"))
    print()

    print("--- Task 2 (calculate_price) ---")
    print(f"Default (1 item, 0 discount): ${calculate_price(100)}")
    print(f"3 items, $10 discount: ${calculate_price(100, 3, 10)}")
    print()

    print("--- Task 3 & 4 (create_profile & reordered keywords) ---")
    profile = create_profile(active=False, city="New York", name="Charlie")
    print(f"Profile with reordered arguments: {profile}")


    print("\n\n--- Part D: Task 1 (Calculate Total) ---")
    nums = [10, 20, 30, 40]
    print(f"Total of {nums}: {calculate_total(nums)}\n")

    print("--- Task 2 (Count Even) ---")
    print(f"Even numbers count in {nums}: {count_even(nums)}\n")

    print("--- Task 3 ---")
    words_list = ["apple", "cat", "banana", "dog", "elephant"]
    print(f"Words >= 5 letters: {get_long_words(words_list, 5)}\n")

    print("--- Tasks 4 & 5 (Students Data) ---")
    students_data = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 92},
        {'name': 'Charlie', 'score': 78}
    ]
    found = find_student(students_data, 'Bob')
    print(f"Find 'Bob': {found}")
    print(f"Average score: {average_score(students_data):.2f}\n")

    print("--- Task 6 (Active Users) ---")
    users_data = [
        {'username': 'alex', 'active': True},
        {'username': 'john', 'active': False},
        {'username': 'mary', 'active': True}
    ]
    print(f"Active users: {get_active_users(users_data)}")


    print("\n\n--- Part E. TASK 1: TEMPERATURE REPORT ---")
    print(format_report(10))
    print()

    print("--- TASK 2: ORDER CALCULATION ---")
    print(f"Total: {get_final_total(order)}")
    print()

    print("--- TASK 3: REFACTORED EXERCISE ---")
    scores_list = [45, 78, 90, 52, 88]
    print(f"Passing average: {calculate_passing_average(scores_list):.2f}")


    print("\n\n--- Part F ---")
    print(f"Total Expected Registration Revenue: ${calculate_total_revenue(participant_list)}\n")
    
    students = get_student_participants(participant_list)
    print(f"--- Student Participants ({len(students)}) ---")
    for student in students:
        print(create_participant_summary(student))
    print()

    oldest = get_oldest_participant(participant_list)
    print("--- Oldest Participant ---")
    if oldest:
        print(create_participant_summary(oldest))


    print("\n\n--- Part G: Task 1 ---")
    test_numbers = [15, 3, 42, -7, 8, 23]
    minimum, maximum = get_min_and_max(test_numbers)
    print(f"Min: {minimum}, Max: {maximum}")

    print("\n--- Task 2 (Palindrome) ---")
    test_word = "radar"
    print(f"Is '{test_word}' a palindrome? {is_palindrome(test_word)}")

    print("\n--- Task 3 (Character Frequencies) ---")
    sample_text = "hello"
    print(f"Frequencies in '{sample_text}': {count_character_frequencies(sample_text)}")

    print("\n--- Task 4 (Number Types Count) ---")
    num_list = [10, -5, 0, 3, -1, 0, 7]
    print(f"Counts for {num_list}: {count_number_types(num_list)}")


main()