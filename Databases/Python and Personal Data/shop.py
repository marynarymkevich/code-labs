from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "webshop.db"

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    try:
        price = float(input("Price: "))
    except ValueError:
        print("Invalid input! Price must be a number.")
        return
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")


def change_stock(conn):
    product_id = int(input("Product ID: "))
    new_stock = int(input("New stock: "))

    conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?",
        (new_stock, product_id),
    )
    conn.commit()
    print("Stock updated!")


def show_receipt(conn):
    order_id = int(input("Order ID: "))
    query = """
        SELECT p.name, oi.quantity, p.price, (oi.quantity * p.price) AS total
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        WHERE oi.order_id = ?
    """
    cursor = conn.execute(query, (order_id,))
    rows = cursor.fetchall()

    for name, quantity, price, total in rows:
        print(f"{name}: {quantity} x {price} kr = {total} kr")


def top_products(conn):
    query = """
        SELECT p.name, SUM(oi.quantity) AS total_sold
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY oi.product_id
        ORDER BY total_sold DESC
        LIMIT 3
    """
    cursor = conn.execute(query)
    rows = cursor.fetchall()

    print("\n--- Top 3 Best-Selling Products ---")
    for name, total_sold in rows:
        print(f"{name} {total_sold} sold")
    print()

def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product  4) Change stock  5) Show receipt  6) Top 3 products  0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        elif choice == "4":
            change_stock(conn)
        elif choice == "5":
            show_receipt(conn)
        elif choice == "6":
            top_products(conn)
        elif choice == "0":
            break
    conn.close()


main()
