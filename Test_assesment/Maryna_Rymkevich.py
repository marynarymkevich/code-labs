# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
def get_info(items):
    info = {
        'total': 0, 
        'highest price name': None
    }
    if not items:
        return info

    max_price = None
    for item in items:
        if item['stock']:
            print(item['name'])
            info['total'] += item['price']*item['stock']
            if max_price is None or item['price'] > max_price:
                max_price = item['price']
                info['highest price name'] = item['name']
    return info

print(get_info(products))


# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:
def calculate_average(scores):
    return round(sum(scores) / len(scores), 2) if scores else 0

def create_result(scores):
    if calculate_average(scores) >= 70:
        return "PASS"
    else:
        return "FAIL"

print('Average: ', calculate_average(scores))
print('Result: ', create_result(scores))



# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:
def calculate_order(name, *prices, **settings):
    subtotal = sum(prices)
    discount = settings.get('discount', 0)
    shipping = settings.get('shipping', 0)
    final_total = subtotal - subtotal * discount / 100 + shipping

    return {
        'customer': name,
        'subtotal': subtotal,
        'final_total': final_total,
        'settings': settings
    }

print(calculate_order('Anna', *product_prices, **order_settings))



# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
def get_formmated_name(name):
    return name.strip().title()

def get_formmated_name_list(players):
    return [get_formmated_name(player['name']) for player in players]

print(get_formmated_name_list(players))

def get_active_players(players):
    return [player for player in players if player['active'] and player['score'] >= 80]

print(get_active_players(players))

def get_sorted_list(players):
    return sorted(players, key=lambda player: player['score'], reverse=True)

def print_list(players):
    sorted_players = get_sorted_list(players)
    
    for index, player in enumerate(sorted_players, start=1):
        name = get_formmated_name(player['name'])
        print(f"{index}. {name} - {player['score']}")

print_list(players)

def print_name_score_list(players):
    names = [get_formmated_name(player['name']) for player in players]
    scores = [player['score'] for player in players]
    for name, score in zip(names, scores):
        print(f"{name}: {score}")

print_name_score_list(players)