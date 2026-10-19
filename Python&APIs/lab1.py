from api_client import get_json

products = get_json("https://fakestoreapi.com/products")

if products:
    sorted_products = sorted(products, key=lambda x: x["price"])
    for product in sorted_products:
        print(f"${product['price']} - {product['title']}")


categories = get_json("https://fakestoreapi.com//products/categories")
for category in categories:
        print(f"${category}")

user_category = input("Enter the category: ").strip()
products_by_category = get_json(f"https://fakestoreapi.com/products/category/{user_category}")
if products_by_category:
    print(f"Total products in category: {len(products_by_category)}")
    cheapest = min(products_by_category, key = lambda x: x["price"])
    print(f"Cheapest product: {cheapest['title']} (${cheapest['price']})")
else:
    print("Category not found or contains no products.")