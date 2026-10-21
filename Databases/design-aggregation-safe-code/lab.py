from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# Ex 1. I would embed the reviews because they are always read together with the book's page. 
# I would reference the members because many members borrow the same book and their profile data is shared

# Ex 2. An advantage of copying the product name into each item is that the order keeps the original name if the product name changes later. 
# A disadvantage is that if there is a mistake in the product name, you have to update it in many orders instead of just one.

# Ex 3. 
# db.create_collection(
#     "newsletter_signups",
#     validator={
#         "$jsonSchema": {
#             "required": ["email", ],
#             "properties": {
#                 "email": {"bsonType": "string"},
#                 "source": {
#                     "bsonType": "string",
#                     "enum": ["web", "store"],
#                 },
#             }
#         }
#     }
# )

valid_doc = {"email": "marina2@gmail.com", "source": "web"}

try:
    db.newsletter_signups.insert_one(valid_doc)
    print("Valid insert succeeded!")
except Exception as e:
    print(f"Valid insert failed: {e}")

invalid_doc = {"email": "bad_user@example.com", "source": "app"}

try:
    db.newsletter_signups.insert_one(invalid_doc)
    print("Invalid insert succeeded (UNEXPECTED)!")
except:
    print("Invalid insert failed as expected!")


# Ex 4
cities = db.customers.aggregate([
    {
        "$group": {
            "_id": "$city",
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"count": -1}
    }
])

for row in cities:
    print(row)


# Ex 5. 
results = db.products.aggregate([
    {
        "$group": {
            "_id": "$category",
            "cheapest": {"$min": "$price"},
            "most_expensive": {"$max": "$price"}
        }
    }
])

for row in results:
    print(row)


# Ex 6.
orders = db.orders.aggregate([
    {
        "$group": {
            "_id": "$customer_id",
            "count": {"$sum": 1}
        }
    }, 
    {
        "$match": {
            "count": {"$gte": 2}
        }
    }
])

print(f"\n Customers with 2 or more orders:")
for order in orders:
    print(f"{order}")


# Ex 7.
order_item_counts = db.orders.aggregate([
    {
        "$project": {
            "item_count": {"$size": "$items"}
        }
    }
])

print("\nNumber of items per order:")
for row in order_item_counts:
    print(row)


# Ex 8.
sold_per_category = db.orders.aggregate([
    {
        "$match": {"status": {"$ne": "cancelled"}}
    },
    {
        "$unwind": "$items"
    },
    {
        "$lookup": {
            "from": "products",
            "localField": "items.product_id",
            "foreignField": "_id",
            "as": "product_info"
        }
    },
    {
        "$unwind": "$product_info"
    },
    {
        "$group": {
            "_id": "$product_info.category",
            "total_sold": {"$sum": "$items.quantity"}
        }
    }
])

print("\nUnits sold per category:")
for row in sold_per_category:
    print(row)


# Ex 9.
revenue_by_status = db.orders.aggregate([
    {
        "$unwind": "$items"
    },
    {
        "$group": {
            "_id": "$status",
            "total_revenue": {
                "$sum": {
                    "$multiply": ["$items.quantity", "$items.unit_price"]
                }
            }
        }
    }
])

print("\nRevenue per status:")
for row in revenue_by_status:
    print(row)


# Ex 10.
popular_tags = db.products.aggregate([
    {
        "$unwind": "$tags"
    },
    {
        "$group": {
            "_id": "$tags",
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"count": -1}
    }
])

print("\nMost common tags:")
for row in popular_tags:
    print(row)