from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# print('--- Exersice 1 ---')
# products = db.products.find({"category": "Accessories"})

# for index, product in enumerate(products, start=1):
#     print(f"{index}: {product['name']}")


# customers = db.customers.find({"city": "Göteborg"})

# print('\n--- Exersice 2 ---')
# for index, customer in enumerate(customers, start=1):
#     print(f"{index}: {customer['first_name']} {customer['last_name']}")


# print('\n--- Exersice 3 ---')
# products = db.products.find()

# for index, product in enumerate(products, start=1):
#     print(f"{index}: {product['name']} - {product['price']} kr")


# count = db.customers.count_documents({"city": "Uppsala"})

# print('\n--- Exercise 4 ---')
# print(f"Customers in Uppsala: {count}")


# print('\n--- Exersice 5 ---')
# product = db.products.find_one({"name": "Sandals"})
# print(product['stock'])


# print('\n--- Exersice 6 ---')
# customers = db.customers.find({"newsletter": True})
# for index, customer in enumerate(customers, start=1):
#     print(f"{index}: {customer['first_name']}")


# print('\n--- Exersice 7 ---')
# result = db.customers.insert_one({"firts_name": "Maryna", "last_name": "Rymkevich", "email": "marina@test.com"})
# print("Inserted ID:", result.inserted_id)

# my_row = db.customers.find_one({"email": "marina@test.com"})
# pprint(my_row)


# print('\n--- Exersice 8 ---')
# new_products = [
#     {
#         "_id": 13,
#         "name": "Cap",
#         "category": "Accessories",
#         "price": 15,
#         "stock": 50,
#         "tags": ["bestseller", "summer"]
#     },
#     {
#         "_id": 14,
#         "name": "Scarf",
#         "category": "Accessories",
#         "price": 25,
#         "stock": 30,
#         "tags": ["winter", "cotton"]
#     }
# ]

# db.products.insert_many(new_products)
# total_products = db.products.count_documents({})
# print(total_products)


# print('\n--- Exersice 9 ---')
# customers = db.customers.find()
# for index, customer in enumerate(customers, start=1):
#     first = customer.get("first_name", "")
#     last = customer.get("last_name", "")
#     city = customer.get("city", "unknown")
    
#     print(f"{index}. {first} {last} ({city})")


print('\n--- Exersice 10 ---')
orders = db.orders.find()

for order in orders:
    print(f"Order {order.get('_id')}: {len(order.get('items'))} items")