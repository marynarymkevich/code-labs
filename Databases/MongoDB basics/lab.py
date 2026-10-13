from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

print('--- Exersice 1 ---')
products = db.products.find({'category': 'Accessories'})

for index, product in enumerate(products, start=1):
    print(f"{index}: {product['name']}")


customers = db.customers.find({'city': 'Göteborg'})

print('\n--- Exersice 2 ---')
for index, customer in enumerate(customers, start=1):
    print(f"{index}: {customer['first_name']} {customer['last_name']}")


print('\n--- Exersice 3 ---')
products = db.products.find()

for index, product in enumerate(products, start=1):
    print(f"{index}: {product['name']} - {product['price']} kr")


count = db.customers.count_documents({"city": "Uppsala"})

print('\n--- Exercise 4 ---')
print(f"Customers in Uppsala: {count}")