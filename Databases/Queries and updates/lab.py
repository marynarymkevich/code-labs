from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

print("--- Exercise 1 ---")
products = db.products.find({"price": {"$gt": 1000}})

for product in products:
    print(f"{product['name']}: {product['price']} kr")


print("\n---- Exercise 2 ---")
orders = db.orders.find({"status": {"$ne": "delivered"}})

for order in orders:
    print(f"Order {order['_id']}: {order['status']}")


print("\n---- Exercise 3 ---")
customers = db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}})

for customer in customers:
    print(f"{customer['first_name']} {customer['last_name']} ({customer['city']})")


print("\n--- Exercise 4 ---")
white_products = db.products.find({"details.color": "white"})

for product in white_products:
    print(f"{product['name']} (Color: {product['details']['color']})")


print("\n--- Exercise 5 ---")
products = db.products.find(
    {"tags": "sport"},
    {"name": 1, "tags": 1, "_id": 0}
)

for product in products:
    print(product)


print("\n--- Exercise 6 ---")
products = db.products.find({}, {"name": 1, "price": 1, "_id": 0}).sort("price", 1).limit(5)
for product in products:
    print(product)


print("\n---- Exercise 7 ---")
orders = db.orders.find({"items.product_id": 2})
for order in orders:
    print(f"Order {order['_id']}: {order['items']}")