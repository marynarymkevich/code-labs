# ================ Part C - Inheritance fundamentals =============

# 1 - 4. Accounts
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class SavingAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

kid_account = SavingAccount('Kid', 200, 1.5)
family_account = SavingAccount('Dad', 30000, 2)

print(f"----- ACOUNTS -------")
print(f"Kid's account owner: {kid_account.owner} with balance: {kid_account.balance}, rate: {kid_account.interest_rate}")
print(f"Family's account owner: {family_account.owner} with balance: {family_account.balance}, rate: {family_account.interest_rate}")


# 5. "is-a" statement explaining why this inheritance relationship makes sense:
# A SavingsAccount IS-A specific type of Account. 
# It inherits all from an Account (owner,balance, etc) 
# and can extend Acount with own features (like an interest rate).



# =========== Part E - super() and shared initialization =========

# 1 - 4. Create a base class Device with brand and year
class Device:
    def __init__(self, brand, year):
        self.brand = brand
        self.is_active = True

        # year cannot be negative
        if year < 0:
            raise ValueError("Year cannot be negative!")
        
        self.year = year
       
        
class Laptop(Device):
    def __init__(self, brand, year, ram_gb):
        super().__init__(brand, year)
        self.ram_gb = ram_gb

class Phone(Device):
    def __init__(self, brand, year, screen_size):
        super().__init__(brand, year)
        self.screen_size = screen_size

marinas_laptop = Laptop("Mac", 2022, 512)
marinas_phone = Phone("Pixel", 2025, 5.6)

# 5. Both subclasses receive the shared initialization logic from Device without duplicating
print(f"\n-------- Devices comparing ----------")
print(f"Device: {marinas_laptop.brand}, {marinas_laptop.year}, Ram: {marinas_laptop.ram_gb}, Active status: {marinas_laptop.is_active} ")
print(f"Device: {marinas_phone.brand}, {marinas_phone.year}, Screen: {marinas_phone.screen_size}, Active status: {marinas_phone.is_active} ")



# ========== Part H - Applied challenge: User accounts ===============

class User:
    def __init__(self, username, email):
        self.username = username

        if '@' not in email:
            raise ValueError("Invalid email!")  # will break the programm 
        
        self.email = email

    def create_nickname(self):
        self.nickname = self.username.lower()[:3] + '_nick'
        return self.nickname


class AdminUser(User):
    def __init__(self, username, email, department):
        super().__init__(username, email)
        self.department = department

    def block_user(self, block_username):
        print(f"User {block_username} is blocked!")

    def create_nickname(self):
        return super().create_nickname() + '_admin'


class PremiumUser(User):
    def __init__(self, username, email, title):
        super().__init__(username, email)
        self.title = title

    def welcome_message(self):
        print(f"Welcome, {self.title} {self.username}")

    def create_nickname(self):
        return self.title.lower() + "_" + super().create_nickname()


standard_user = User("Bob", "bob@mail.com")
tech_admin = AdminUser("John", "john@mail.com", "Tech")
premium_guest = PremiumUser("Alex", "alex@mail.com", "Mr")

print(f"\n-------- USERS COMPARING ----------")
print(f"User nickname: {standard_user.create_nickname()}")
print(f"Admin nickname: {tech_admin.create_nickname()}")
print(f"Premium user nickname: {premium_guest.create_nickname()}")

print(f"\n-------- SUBCLASS METHODS ----------")
tech_admin.block_user("BadUser99")
premium_guest.welcome_message()
 