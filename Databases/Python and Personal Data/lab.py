import sqlite3

## Exercise 1
conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

cursor.execute("SELECT first_name, last_name, city FROM customers")
rows = cursor.fetchall()

for index, (first_name, last_name, city) in enumerate(rows, start=1):
    print(f"{index}. {first_name} {last_name} ({city})")


## Exercise 2
# max_price = float(input("Enter max price: "))

# query = "SELECT name, price FROM products WHERE price < ?"
# cursor.execute(query, (max_price,))
# products = cursor.fetchall()

# for name, price in products:
#     print(f"{name} - ${price}")


## Exercise 3
category = input("Enter a category: ")

query = "SELECT COUNT(*) FROM products WHERE category = ?"
cursor.execute(query, (category,))
result = cursor.fetchone()
##print(result)
product_count = result[0]

print(f"Number of products in '{category}': {product_count}")

## Exercise 4
# building SQL with an f-string is dangerous because it allows someone to insert their own code. 
# This code can then modify, steal, or delete data from our database
# A ? placeholder is safe because it keeps user input separate from SQL code.
# The database treats the input only as simple data