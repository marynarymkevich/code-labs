# =============================================================================
# Part A - List comprehensions
# =============================================================================

# 1. Squares for numbers 1-20
squares_loop = []

for number in range(1, 21):
    squares_loop.append(number ** 2)
print("normal loop:", squares_loop)

squares_comprehension = [number ** 2 for number in range(1, 21)]
print("list comprehension:", squares_comprehension)


# 2. Even numbers from 1-100
even_numbers = [number for number in range(1, 101) if number % 2 == 0]
print("even numbers:", even_numbers)


# 3. Stripped title-cased names
names = ["  alice ", "BOB", "  charlie brown ", "DIANA"]
stripped_title_cased_names = [name.strip().title() for name in names]
print("original names:", names)
print("stripped, title-cased names:", stripped_title_cased_names)


# 4. Passing scores
scores = [42, 55, 70, 81, 39, 90, 60, 59]
passing_scores = [score for score in scores if score >= 60]
print("scores:", scores)
print("passing scores:", passing_scores)


# 5. PASS/FAIL
pass_fail_labels = ["PASS" if score >= 60 else "FAIL" for score in scores]
print("labels:", pass_fail_labels)



# 6. Rewrite three earlier loop-based transformations as comprehensions
# example 1
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 88},
]

names = []
for student in students:
    names.append(student["name"])
names_compr = [student["name"] for student in students]

# example 2
prices = [100, 250, 400, 80]
discounted_prices = []
for price in prices:
    discounted_prices.append(price * 0.9)

discounted_prices = [price * 0.9 for price in prices]

# example 3
words = ["python", "is", "awesome", "a", "code"]
long_words_upper = []
for word in words:
    if len(word) > 3:
        long_words_upper.append(word.upper())

long_words_upper = [word.upper() for word in words if len(word) > 3]



# =============================================================================
# Part B - Dictionary and set comprehensions
# =============================================================================

# 1. Dictionary mapping numbers 1-10 to their squares
squares_dict = {number: number ** 2 for number in range(1, 11)}
print("squares dictionary:", squares_dict)


# 2. Dictionary mapping each word to its length
words = ["apple", "banana", "kiwi", "strawberry"]
word_to_length = {word: len(word) for word in words}
print("word to length:", word_to_length)


# 3. Set comprehension with lowercase values
values_with_duplicates = ["Apple", " banana ", "APPLE", "Banana", "KIWI", " kiwi"]
lowercase_normalized_values = {value.strip().lower() for value in values_with_duplicates}
print("original values:", values_with_duplicates)
print("lowercase normalized values:", lowercase_normalized_values)


# 4. Dictionary of products
products = {
    "milk": 1.20,
    "bread": 2.50,
    "cheese": 4.80,
    "apples": 1.90,
    "coffee": 6.40,
}
chosen_threshold = 3.00
products_below_threshold = {
    product_name: price
    for product_name, price in products.items()
    if price < chosen_threshold
}
print("chosen threshold:", chosen_threshold)
print("products below threshold:", products_below_threshold)


# 5. Dictionary mapping student names to PASS/FAIL
student_dictionaries = [
    {"name": "Alice", "score": 82},
    {"name": "Bob", "score": 54},
    {"name": "Charlie", "score": 60},
    {"name": "Diana", "score": 47},
]
student_names_to_pass_fail = {
    student["name"]: ("PASS" if student["score"] >= 60 else "FAIL")
    for student in student_dictionaries
}
print("student names to PASS/FAIL:", student_names_to_pass_fail)


# =============================================================================
# Part C - enumerate
# =============================================================================

# 1. Playlist with numbering starting at 1
playlist = ["Bohemian Rhapsody", "Imagine", "Billie Jean", "Hey Jude"]
for number, song in enumerate(playlist, start=1):
    print(f"{number}. {song}")


# 2. Task 1, Task 2
tasks = ["Open the file", "Clean the data", "Print the report"]
for number, task in enumerate(tasks, start=1):
    print(f"Task {number}: {task}")


# 3. Indexes of all values above a threshold
values = [12, 45, 67, 23, 89, 34, 90, 15]
threshold = 50
indexes_above_threshold = [index for index, value in enumerate(values) if value > threshold]
print("values:", values)
print("threshold:", threshold)
print("indexes of all values above a threshold:", indexes_above_threshold)


# 4. Rewrite a range(len(...)) loop using enumerate
items = ["pen", "notebook", "eraser"]

print("range(len(...)) version:")
for index in range(len(items)):
    print(index, items[index])

print("enumerate version:")
for index, item in enumerate(items):
    print(index, item)

# Why the new version is clearer: enumerate visual clean, no need for items[index]



# =============================================================================
# Part D - zip and unpacking
# =============================================================================

# 1. Combine separate name and score lists using zip
name_list = ["Alice", "Bob", "Charlie", "Diana"]
score_list = [82, 54, 60, 47]
for name, score in zip(name_list, score_list):
    print(name, score)


# 2. Create a dictionary using dict(zip(keys, values))
keys = ["Alice", "Bob", "Charlie", "Diana"]
values = [82, 54, 60, 47]
name_to_score = dict(zip(keys, values))
print("dict(zip(keys, values)):", name_to_score)


# 3. Combine three lists: product name, price and stock
product_name = ["milk", "bread", "cheese"]
price = [1.20, 2.50, 4.80]
stock = [12, 8, 3]
for name, product_price, product_stock in zip(product_name, price, stock):
    print(name, product_price, product_stock)


# 4. Investigate what happens when zipped lists have different lengths
short_list = ["Alice", "Bob"]
long_list = [82, 54, 60, 47]
print("short list:", short_list)
print("long list:", long_list)
print("zip result:", list(zip(short_list, long_list)))
# extra values from the longer list are ignored


# 5. Tuple unpacking directly in a for loop over zipped data
for name, score in zip(name_list, score_list):
    print(f"{name}: {score}")


# 6. Swap two variables without a temporary variable
first = "Alice"
second = "Bob"
print("before swap:", first, second)
first, second = second, first
print("after swap:", first, second)


# =============================================================================
# Part E - sorted and lambda
# =============================================================================

# 1. Sort a list of words by length
words = ["strawberry", "kiwi", "banana", "fig", "apple"]
words_sorted_by_length = sorted(words, key=len)
print("words:", words)
print("sorted by length:", words_sorted_by_length)


# 2. Sort student dictionaries by score ascending and descending
student_dictionaries = [
    {"name": "Alice", "score": 82},
    {"name": "Bob", "score": 54},
    {"name": "Charlie", "score": 60},
    {"name": "Diana", "score": 47},
]
by_score_ascending = sorted(student_dictionaries, key=lambda student: student["score"])
by_score_descending = sorted(
    student_dictionaries, key=lambda student: student["score"], reverse=True
)
print("score ascending:", by_score_ascending)
print("score descending:", by_score_descending)


# 3. Sort products by price using a lambda
products = [
    {"product_name": "milk", "price": 1.20},
    {"product_name": "bread", "price": 2.50},
    {"product_name": "cheese", "price": 4.80},
    {"product_name": "apples", "price": 1.90},
]
products_sorted_by_price = sorted(products, key=lambda product: product["price"])
print("products sorted by price:", products_sorted_by_price)


# 4. Sort people by last_name
people = [
    {"first_name": "Alice", "last_name": "Brown"},
    {"first_name": "Bob", "last_name": "Anderson"},
    {"first_name": "Charlie", "last_name": "Clark"},
    {"first_name": "Diana", "last_name": "Adams"},
]
people_sorted_by_last_name = sorted(people, key=lambda person: person["last_name"])
print("people sorted by last_name:", people_sorted_by_last_name)


# 5. Named function for a sort key, then replace it with lambda
products = [
    {"product_name": "milk", "price": 1.20, "stock": 12},
    {"product_name": "bread", "price": 2.50, "stock": 8},
    {"product_name": "cheese", "price": 4.80, "stock": 3},
]

def inventory_value(product):
    return product["price"] * product["stock"]

sorted_with_named_function = sorted(products, key=inventory_value)
sorted_with_lambda = sorted(products, key=lambda product: product["price"] * product["stock"])
print("named function:", sorted_with_named_function)
print("lambda:", sorted_with_lambda)
# Named function is clearer when the key has a name/meaning or more than one expression.
# Lambda is clearer for a short one-line key such as product["price"].



# =============================================================================
# Part F - Applied challenge: Data cleanup
# =============================================================================

# 1. Start with a list of at least twelve messy dictionaries
messy_products = [
    {"name": "  milk", "category": "DAIRY", "price": 1.20, "stock": 12},
    {"name": "BREAD ", "category": " bakery", "price": 2.50, "stock": 8},
    {"name": " cheddar cheese", "category": "Dairy", "price": 4.80, "stock": 3},
    {"name": "APPLES", "category": "FRUIT", "price": 1.90, "stock": 20},
    {"name": " bananas ", "category": "fruit", "price": 1.50, "stock": 0},
    {"name": "Coffee", "category": " DRINKS", "price": 6.40, "stock": 5},
    {"name": "  TEA", "category": "drinks", "price": 3.10, "stock": 15},
    {"name": "yogurt", "category": "dairy ", "price": 0.90, "stock": 7},
    {"name": " ORANGE juice ", "category": "Drinks", "price": 2.20, "stock": 0},
    {"name": "croissant", "category": "BAKERY", "price": 1.80, "stock": 9},
    {"name": " grapes", "category": " Fruit", "price": 2.70, "stock": 4},
    {"name": "BUTTER", "category": "dairy", "price": 2.10, "stock": 11},
]
print("messy products:", messy_products)


# 2. Create a cleaned list where names/categories are normalized
cleaned_products = [
    {
        'name': product['name'].strip().title(),
        'category': product['category'].strip().title(),
        'price': product['price'],
        'stock': product['stock'],
    }
    for product in messy_products
]
print("cleaned products:", cleaned_products)


# 3. Create a list of in-stock products
in_stock_products = [product for product in messy_products if product['stock'] > 0]
print("in-stock products:", in_stock_products)


# 4. Create a set of unique normalized categories
unique_normalized_categories = {product['category'] for product in cleaned_products}
print("unique normalized categories:", unique_normalized_categories)


# 5. Dictionary mapping product name to inventory value (price * stock)
product_name_to_inventory_value = {
    product['name']: product['price']*product['stock'] 
    for product in cleaned_products
} 
print("product name to inventory value:", product_name_to_inventory_value)


# 6. Sort products by inventory value from highest to lowest
products_sorted_by_inventory_value = sorted(
    cleaned_products, 
    key=lambda product: product['price']*product['stock'] , 
    reverse=True
)
print("sorted by inventory value:", products_sorted_by_inventory_value)


# 7. Use enumerate to print a ranked report
for rank, product in enumerate(products_sorted_by_inventory_value, start=1):
    inventory_value = product["price"] * product["stock"]
    print(
        f"{rank}. {product['name']} | category: {product['category']} | "
        f"price: {product['price']} | stock: {product['stock']} | "
        f"inventory value: {inventory_value:.2f}"
    )


# 8. Use zip to combine at least one pair of separate derived lists
product_names = [product["name"] for product in cleaned_products]
inventory_values = [round(product["price"] * product["stock"], 2) for product in cleaned_products]
name_and_inventory_value = list(zip(product_names, inventory_values))
print("product names zipped with inventory values:", name_and_inventory_value)


# 9. Over-complicated comprehension and a clearer alternative

# over-complicated: too many steps and nested expressions in one line
over_complicated = sorted(
    [
        {
            "name": p["name"].strip().title(),
            "inv_val": round(float(p["price"]) * int(p["stock"]), 2),
        }
        for p in messy_products
        if p.get("stock") and int(p["stock"]) > 0
    ],
    key=lambda x: x["inv_val"],
    reverse=True,
)
print("over-complicated:", over_complicated)

# clearer alternative
clean_in_stock = [
    {
        "name": p["name"].strip().title(),
        "inv_val": round(float(p["price"]) * int(p["stock"]), 2),
    }
    for p in messy_products
    if int(p.get("stock", 0)) > 0
]

clear_version = sorted(
    clean_in_stock, key=lambda p: p["inv_val"], reverse=True
)
print("clearer alternative:", clear_version)
# The clearer version is better because it is simple to read or debug


# =============================================================================
# Part G - Stretch challenges
# =============================================================================

# 1. Flatten a simple list of lists using a comprehension
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = [inner_inner_item for inner_list in list_of_lists for inner_inner_item in inner_list]
print("list of lists:", list_of_lists)
print("flattened:", flattened)


# 2. Multiplication table structure using a nested comprehension
multiplication_table = [
    [row * column for column in range(1, 11)]
    for row in range(1, 11)
]
print("multiplication table:")
for row in multiplication_table:
    print(row)


# 3. Create only passing student dictionaries in one readable comprehension
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
scores = [82, 54, 60, 47, 91]
passing_student_dictionaries = [
    {'name': name, 'score': score}
    for name, score in zip(names, scores)
    if score >= 60
]
print("passing student dictionaries:", passing_student_dictionaries)


# 4. Use any() and all()
scores = [82, 54, 60, 47, 91]

# Question 1: Did all students pass the exam (score >= 60)?
# Question 2: Is there at least one student with an excellent score (score >= 90)?

# loops
all_passed_loop = True
for score in scores:
    if score < 60:
        all_passed_loop = False
        break

has_top_score_loop = False
for score in scores:
    if score >= 90:
        has_top_score_loop = True
        break

print("Loop - All passed:", all_passed_loop)
print("Loop - Has top score:", has_top_score_loop)

# Using any() and all()
all_passed = all(score >= 60 for score in scores)
has_top_score = any(score >= 90 for score in scores)

print("any/all - All passed:", all_passed)
print("any/all - Has top score:", has_top_score)

# 5. Five examples where Pythonic syntax reduces boilerplate without reducing clarity

# Example 1: Swap variables without a temporary third variable
a, b = 5, 10
a, b = b, a

# Example 2: Unpacking elements directly
point = (3, 4)
x, y = point

# Example 3: Dictionary get() with a default value
user_status = {}
role = user_status.get("role", "guest")

# Example 4: Enumerate
for index, item in enumerate(items):
    print(index, item)

# Example 5: List comprehension with condition
even_squares = [
    x**2 for x in range(10) if x % 2 == 0
]