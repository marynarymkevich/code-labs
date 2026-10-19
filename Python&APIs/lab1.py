from api_client import get_json
import requests

BASE_URL = "https://fakestoreapi.com/products"
products = get_json(BASE_URL)

if products:
    sorted_products = sorted(products, key=lambda x: x["price"])
    for product in sorted_products:
        print(f"${product['price']} - {product['title']}")


categories = get_json(f"{BASE_URL}/categories")
for category in categories:
        print(f"{category}")

user_category = input("Enter the category: ").strip()
products_by_category = get_json(f"{BASE_URL}/category/{user_category}")
if products_by_category:
    print(f"Total products in category: {len(products_by_category)}")
    cheapest = min(products_by_category, key = lambda x: x["price"])
    print(f"Cheapest product: {cheapest['title']} (${cheapest['price']})")
else:
    print("Category not found or contains no products.")


## Task 4
new_product = {
    "title": "Test product",
    'price': 13.5,
    'description': 'A product we create from Python',
    'image': 'https://champion.se/thumb/916/2560x0/CHBR220_1.webp',
    'category': 'electronics',
}

response_post = requests.post(BASE_URL, json=new_product, timeout=5)
print(f"POST Status Code: {response_post.status_code}")
print(f"POST Answer: {response_post.json()}")

product_id = 7
updated_data = {"price": 29.99}

response_patch = requests.patch(f"{BASE_URL}/{product_id}", json=updated_data, timeout=5)
print(f"PATCH Status Code: {response_patch.status_code}")
print(f"PATCH Answer: {response_patch.json()}")


## Task 5
# 1. Wrong URL
get_json("https://fakestoreapi.com/wrong-endpoint")

# 2. Timeout
get_json(BASE_URL, timeout=0.001)

# 3. Bad domain
get_json("https://this-domain-does-not-exist.com")