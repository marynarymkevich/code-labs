# ======= Part A - Scope ====================================

# 1. Global vs Local with same name
course_name = "Global Python Course"

def show_scope():
    course_name = "Local Data Science Course"
    print("Inside function (local):", course_name)

show_scope()
print("Outside function (global):", course_name)
# Local variable is inside show_scope(), 
# so the global variable remains unchanged


# 2. Local counter unavailable outside
def count_items():
    item_count = 10
    print("Item count inside:", item_count)

count_items()
# print(item_count)  # NameError: name 'item_count' is not defined


# 3. Modifying global numeric variable via return
score = 50

# modifying without 'global' causes UnboundLocalError:
# def bad_ex_increase():
#     score = score + 10

def increase_score(current_score, points):
    return current_score + points

score = increase_score(score, 15)
print("Updated score via return:", score)


# 4. Nested function and enclosing scope
def outer_function():
    category = "Programming"
    
    def inner_function():
        print("Enclosing category:", category)
        
    inner_function()
outer_function()


# 5. Avoiding shadowing built-in names
# Do not use names like list, str, sum, max
numbers_list = [10, 20, 30]
text_string = "Hello"
total_sum = sum(numbers_list)
maximum_val = max(numbers_list)
print("Built-ins preserved:", total_sum, maximum_val)



# ======== Part B - *args =============

# 1. Add all numbers without sum()
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("add_all(5, 10, 15):", add_all(5, 10, 15))


# 2. Average with empty check
def average(*numbers):
    if not numbers:
        return 0.0
    return add_all(*numbers) / len(numbers)

print("average(10, 20, 30):", average(10, 20, 30))
print("average():", average())


# 3. Longest word
def longest_word(*words):
    if not words:
        return ""
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print("Longest word:", longest_word("apple", "banana", "watermelon", "kiwi"))


# 4. Build sentence with separator
def build_sentence(separator, *words):
    return separator.join(words)

print("Sentence:", build_sentence("-", "Python", "is", "awesome"))


# 5. Describe scores
def describe_scores(student_name, *scores):
    count = len(scores)
    avg_score = average(*scores)
    return student_name, count, avg_score

name, count, avg = describe_scores("Alice", 85, 90, 95)
print(f"Student: {name}, Count: {count}, Average: {avg}")



# ========== Part C - Positional unpacking ===============================

# 1. Unpack list
def show_point(x, y, z):
    print(f"Point coordinates: x={x}, y={y}, z={z}")

point_list = [10, 20, 30]
show_point(*point_list)


# 2. Unpack tuple
def print_user_info(first_name, last_name, city):
    print(f"{first_name} {last_name} lives in {city}")

user_tuple = ("John", "Doe", "London")
print_user_info(*user_tuple)


# 3. Starred assignment
values1 = [1, 2, 3, 4, 5]
first, *middle, last = values1
print(f"First: {first}, Middle: {middle}, Last: {last}")

values2 = [100, 200]
first, *middle, last = values2
print(f"Short list - First: {first}, Middle: {middle}, Last: {last}")


# 4. Explanation In definition: def func(*args) packs arguments into tuple.
# In call: func(*my_list) unpacks elements to separate arguments.



# ======== Part D - **kwargs ==================

# 1. Show profile
def show_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_profile(name="Bob", age=25, job="Developer")


# 2. Create user
def create_user(username, **details):
    user_dict = {"username": username}
    user_dict.update(details)
    return user_dict
print("Created user:", create_user("alex99", email="marina@test.com", role="admin"))


# 3. Build product
def build_product(name, price, **metadata):
    return {
        "name": name,
        "price": price,
        "metadata": metadata
    }

print("Product:", build_product("Laptop", 1200, brand="Dell", warranty="2 years"))


# 4. Filter settings (ignore None)
def clean_settings(**settings):
    cleaned = {}
    for key, value in settings.items():
        if value is not None:
            cleaned[key] = value
    return cleaned

print("Cleaned settings:", clean_settings(theme="dark", font=None, volume=80))


# 5. Unpack dictionary into normal parameters
def set_display(width, height, color):
    print(f"Display: {width}x{height}, Color: {color}")

display_config = {"width": 1920, "height": 1080, "color": "black"}
set_display(**display_config)



# ========= Part E - Combining parameters ============================

# 1. Log event
def log_event(event_type, *messages, **metadata):
    return {
        "event_type": event_type,
        "messages": messages,
        "metadata": metadata
    }

print(log_event("ERROR", "Connection lost", "Retry failed", server="Server-1", code=500))


# 2. Calculate order
def calculate_order(customer, *prices, **options):
    subtotal = sum(prices)
    discount = options.get("discount", 0)
    shipping = options.get("shipping", 0)
    
    total = subtotal - discount + shipping
    return {
        "customer": customer,
        "subtotal": subtotal,
        "final_total": total
    }

print("Order result:", calculate_order("Mary", 50, 100, 30, discount=10, shipping=15))


# 3. Explicit named parameters vs **kwargs

# with **kwargs
def set_user_kw(**kwargs):
    return kwargs.get("name"), kwargs.get("age")

# Explicit version (clearer)
def set_user_explicit(name, age):
    return name, age

# Explanation: Explicit parameters are clearer because anyone reading the function 
# signature immediately knows what inputs are required without reading the body.


# 4. Three different calls to flexible function
def process_data(action, *items, **options):
    print(f"Action: {action} | Items count: {len(items)} | Options count: {len(options)}")

process_data("clean")
process_data("filter", 10, 20, 30)
process_data("export", "file1.txt", "file2.txt", format="pdf", overwrite=True)



# ========== Part F - Report builder =================

# 1-3. Create report
def create_report(title, *sections, **metadata):
    return {
        'title': title,
        'sections': sections,
        'metadata': metadata
    }

report = create_report(
    "Math report",
    "Introduction to Python",
    "Data Analysis",
    {"Testing": "Test"},
    author="Maryna",
    department="CS",
    version=1.0,
    confidential=False
)


# 4. Summarize report
def summarize_report(report):
    return (
        f"-- Report ---\n"
        f"Title: {report['title']}\n"
        f"Sections: {report['sections']}\n"
        f"Metadata: {report['metadata']}"
    )

print(summarize_report(report))


# 5. Count words
def count_words(*sections):
    words_total = 0
    
    for section in sections:
        if type(section) == str:
            words_total += len(section.split())
        elif type(section) == dict:
            for sub_section in section.values():
                    if type(sub_section) == str:
                         words_total += len(sub_section.split())

    return words_total

total = count_words(*report['sections'])
print(f"Total words: {total}")


# Dictionary unpacking
default_meta = {
    'author': 'Alex Morgan',
    'department': 'Data Science',
    'version': 1.0
}

strict_meta = {
    'author': 'Elena Rostova',
    'department': 'Security',
    'version': 2.1,
    'confidential': True
}

create_report(
    'Predefined meta', 
    "Introduction to Python",
    "Data Analysis",
    {"Testing": "Test"},
    **default_meta
)

create_report(
    'Predefined meta2', 
    "Introduction to Python",
    "Data Analysis",
    {"Testing": "Test"},
    **strict_meta
)


# 7. Safe way
def set_metadata(metadata_fields, metadata):
    metadata_formatted = {}
    for field in metadata_fields:
        metadata_formatted[field] = metadata.get(field, None)
    return metadata_formatted

     
def summarize_report_safe(report):
    metadata_fields = ('author', 'department', 'version', 'confidential', 'date')
    safe_meta = set_metadata(metadata_fields, report.get('metadata', {}))
    summary = (
            f"-- Report ---\n"
            f"Title: {report['title']}\n"
            f"Sections: {report['sections']}\n"
            f"Metadata: {safe_meta}"
        )
    return summary

print(summarize_report_safe(report))



# ========== Part G - Stretch Challenges =================

# 1. merge_settings
def merge_settings(defaults, **overrides):
    new_dict = defaults.copy()
    for prop in overrides.keys():
        new_dict[prop] = overrides[prop]

    return new_dict   # or shorter {**defaults, **overrides}


# 2. call_summary
def call_summary(function_name, *args, **kwargs):
    args_as_string = str(args)[1:-1] if args else ''
    kwargs_as_string = str(kwargs)[1:-1] if kwargs else ''
    return f"Called {function_name} with args: ({args_as_string}) \nand kwargs: ({kwargs_as_string})"

print(call_summary('create_report', 'math', 'python', author='Alex'))


# 3. Statistics function
def get_statisctics(*numbers):
    statistics = {
        'count': 0,
        'total': 0,
        'average': 0,
        'min': None,
        'max': None,
    }

    if not numbers:
        return statistics
        
    min_val = numbers[0]
    max_val = numbers[0]

    for number in numbers:  
        statistics['total'] += number

        if number < min_val:
            min_val = number

        if number > max_val:
            max_val = number

    statistics['count'] = len(numbers)   
    statistics['average'] = round(statistics['total']/len(numbers), 2)
    statistics['min'] = min_val
    statistics['max'] = max_val

    return statistics

print(f"Statistics: {get_statisctics(*[56, 43, 76, 3, 233])}")


# 4. Predictions
# Local vs Global variable scope
x = 10
def update_val():
    x = 20
update_val()
print(x)  # 10

# Mutating a mutable object in-place
def add_item(data):
    data.append(99)
my_list = [1, 2, 3]
add_item(my_list)
print(my_list)  # [1, 2, 3, 99]

# Modifying global variables via 'global' keyword
count = 0
def increment():
    global count
    count += 5
increment()
print(count)  # 5

# Rebind reference vs in-place mutation
def reset_list(data):
    data = []
my_list = [1, 2, 3]
reset_list(my_list)
print(my_list)  # [1, 2, 3]

# Mutable default parameter persistence
def append_to(element, target=[]):
    target.append(element)
    return target
print(append_to(1))  # [1]
print(append_to(2))  # [1, 2]



