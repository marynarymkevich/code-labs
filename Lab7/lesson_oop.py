# ======== Part A - Classes and objects ===================================

# 1 - 4. Book class with title, author, pages, and a default parameter value
class Book:
    def __init__(self, title, author, pages=100):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

# 1. Create Book objects
book1 = Book("1984", "George Orwell", 328)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
# 4. Using default parameter for pages
book4 = Book("Short Stories", "Various Authors")

print("--- Book Attributes ---")
print(f"Book 1: {book1.title} by {book1.author}, {book1.pages} pages")
print(f"Book 2: {book2.title} by {book2.author}, {book2.pages} pages")
print(f"Book 3: {book3.title} by {book3.author}, {book3.pages} pages")
print(f"Book 4 (default pages): {book4.title} by {book4.author}, {book4.pages} pages")


# 2. Laptop class with brand, model, ram_gb, and price
class Laptop:
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

laptop1 = Laptop("Apple", "MacBook Air", 16, 1200)
laptop2 = Laptop("Dell", "XPS 13", 16, 1100)
laptop3 = Laptop("Lenovo", "ThinkPad", 32, 1400)

print("\n--- Laptop Price Change ---")
print(f"Original price of {laptop1.brand} {laptop1.model}: ${laptop1.price}")

# Change the price of one object
laptop1.price = 1050
print(f"Updated price of {laptop1.brand} {laptop1.model}: ${laptop1.price}")


# 5. Create one object using keyword arguments
laptop_keyword = Laptop(brand="ASUS", model="ROG", ram_gb=32, price=1800)
print(f"Keyword object: {laptop_keyword.brand} {laptop_keyword.model}")


# 3. Create at least two objects with the same attribute values and use 'is' to check identity
laptop_a = Laptop("HP", "Spectre", 16, 1300)
laptop_b = Laptop("HP", "Spectre", 16, 1300)

print("\n--- Object Identity Check ---")
print(f"Are laptop_a and laptop_b the exact same object? {laptop_a is laptop_b}")



# ========== Part B - Methods and state ====================================

# 1. Extend Book class with is_long() method (done above)
# Test Book.is_long()
book_short = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book_long = Book("1984", "George Orwell", 328)

print("--- Book Len Check ---")
print(f"Is '{book_short.title}' long? {book_short.is_long()}")
print(f"Is '{book_long.title}' long? {book_long.is_long()}")


# 2, 3. BankAccount class with deposit() and withdraw() methods
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"Cannot withdraw ${amount} from ${self.balance}")
        self.balance -= amount
        print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

account = BankAccount("Anna", 500)
account.deposit(200)


# 4. Task class with complete() and reopen() methods
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

print("\n--- 4. Task class ---")
task = Task("Prepare Lab7")
print(f"Task '{task.title}' completed: {task.completed}")

task.complete()
print(f"After complete(): {task.completed}")

task.reopen()
print(f"After reopen(): {task.completed}")


# 5. Show that changing state of one object does not change the other
account1 = BankAccount("David", 300)
account2 = BankAccount("Sara", 500)

print("\n--- Independent Object States ---")
print(f"Original balances: David: ${account1.balance}, Sara: ${account2.balance}")

account1.deposit(150)
print(f"After deposit 150 David: ${account1.balance}, Sara: ${account2.balance}")



# ======= Part C =========

# 1 - 4. Products
class Product:
    tax_rate = 20

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return self.price * (100 + self.tax_rate) / 100

product1 = Product("Laptop", 20000)
product2 = Product("Laptop2", 40000)
product3 = Product("Laptop3", 30000)
print(product1.price_with_tax(), product2.price_with_tax(), product3.price_with_tax())


# 5. Change Product.tax_rate
Product.tax_rate = 30
print(f"After tax_rate changing: {product1.price_with_tax(), product2.price_with_tax(), product3.price_with_tax()}")


# 6. Give one Product object its own tax_rate
product3.tax_rate = 50
print(f"Product3 tax_rate: {product3.tax_rate}, Product2 tax_rate: {product2.tax_rate}, Product class tax_rate: {Product.tax_rate}")



# ======= Part D ========================

# 1. Create at least six Student objects, 2. Store all Students in a list
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_status(self):
        return "PASS" if self.score >= 70 else "FAIL"

students = []
students.append(Student("Anna", 50))
students.append(Student("Maria", 60))
students.append(Student("Alex", 800))
students.append(Student("Volha", 70))
students.append(Student("Cristy", 100))
students.append(Student("Bob", 90))


# 3. Loop through the list and print each student's name and score
for student in students:
    print( f"Name: {student.name}, Score: {student.score}")


# 5. Loop and print each student's name and status.
for student in students:
    print(f"Name: {student.name}, Status: {student.get_status()}")


# 6. Create a list containing only students with a score of 70 or higher
highest_score_students = [
    student
    for student in students
    if student.score >= 70
]
for student in highest_score_students:
    print(f"Name: {student.name}, Score: {student.score}, Status: {student.get_status()}")