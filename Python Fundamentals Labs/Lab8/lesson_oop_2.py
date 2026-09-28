# ======== Part A - Mutable default arguments =============================

# 1 - 2. BadTeam class with name and a default parameter members=[]
class BadTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, member_name):
        self.members.append(member_name)


# Test with two BadTeam objects without providing a members list
bad_team1 = BadTeam("Alpha")
bad_team2 = BadTeam("Beta")

bad_team1.add_member("Anna")

print("-------- BAD TEAM ----------")
print(f"Bad Team 1 members: {bad_team1.members}")
print(f"Bad Team 2 members: {bad_team2.members}")

# Explanation:
# What happened: Default parameters are created only once when the class is created
# so both bad_team1 and bad_team2 got the same list in memory
# Adding a member to team 1 also adds it to team 2 (because of the same link to memory slot)


# 3 - 4. Corrected Team class using None as default parameter
class Team:
    def __init__(self, name, members=None):
        self.name = name
        if members is None:
            self.members = []
        else:
            self.members = members

    def add_member(self, member_name):
        self.members.append(member_name)


# Test with two Team objects
good_team1 = Team("Alpha")
good_team2 = Team("Beta")

good_team1.add_member("Anna")

print("\n-------- CORRECTED TEAM (NOT SHARED) ----------")
print(f"Good Team 1 members: {good_team1.members}")
print(f"Good Team 2 members: {good_team2.members}")



# ========== Part B - Dictionary or class? ================================

# 1. Represent a movie using a dictionary
movie_dict = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "rating": 8.8
}

print("-------- MOVIE DICTIONARY ----------")
print(f"Title: {movie_dict['title']}, Rating: {movie_dict['rating']}")


# 2 - 3. Represent movie using a Movie class
class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    # whether the movie is highly rated
    def is_highly_rated(self):
        return self.rating >= 8.0


movie1 = Movie("Inception", "Christopher Nolan", 8.8)
movie2 = Movie("The Room", "Tommy Wiseau", 3.7)

print("\n-------- MOVIE CLASS ----------")
print(f"Is '{movie1.title}' highly rated? {movie1.is_highly_rated()}")
print(f"Is '{movie2.title}' highly rated? {movie2.is_highly_rated()}")


# 4. Explanation:
# A dictionary is for simple data, it has only key-value pairs without any methods
# A class is nessessary when we need custom behavior/methods (like is_highly_rated), validation, etc



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

print(f"\n------------- ACOUNTS -------------------")
print(f"Kid's account owner: {kid_account.owner} with balance: {kid_account.balance}, rate: {kid_account.interest_rate}")
print(f"Family's account owner: {family_account.owner} with balance: {family_account.balance}, rate: {family_account.interest_rate}")


# 5. "is-a" statement explaining why this inheritance relationship makes sense:
# A SavingsAccount IS-A specific type of Account. 
# It inherits all from an Account (owner,balance, etc) 
# and can extend Acount with own features (like an interest rate).



# =========== Part D - Inherited and subclass-specific behaviour =========

class Employee:
    def __init__(self, name):
        self.name = name

    def get_information(self):
        return f"Employee: {self.name}"


class Developer(Employee):
    def write_code(self):
        print(f"{self.name} is writing code...")


class Manager(Employee):
    def conduct_meeting(self):
        print(f"{self.name} is conducting a team meeting...")


dev = Developer("Alex")
mgr = Manager("Sarah")
emp = Employee("John")

print(f"\n-------- INHERITED BEHAVIOR ----------")
print(dev.get_information())
print(mgr.get_information())

print(f"\n-------- SUBCLASS-SPECIFIC METHODS ----------")
dev.write_code()
mgr.conduct_meeting()

# print(f"\n-------- BASE EMPLOYEE LIMITATION ----------")
# Employee object cannot use subclass-specific methods:
# emp.write_code() -----> AttributeError: 'Employee' object has no attribute 'write_code'



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
print(f"\n-------- DEVICES COMPARING ----------")
print(f"Device: {marinas_laptop.brand}, {marinas_laptop.year}, Ram: {marinas_laptop.ram_gb}, Active status: {marinas_laptop.is_active} ")
print(f"Device: {marinas_phone.brand}, {marinas_phone.year}, Screen: {marinas_phone.screen_size}, Active status: {marinas_phone.is_active} ")



# ========== Part F - Method overriding ===================================

# 1 - 4. Notifications objects
class Notification:
    def send(self):
        return "Sending a general notification"


class EmailNotification(Notification):
    def send(self):
        return "Sending email notification to user..."


class SMSNotification(Notification):
    def send(self):
        return "Sending SMS notification to phone..."


general_notif = Notification()
email_notif = EmailNotification()
sms_notif = SMSNotification()

print(f"\n-------- NOTIFICATIONS COMPARING ----------")
print(general_notif.send())
print(email_notif.send())
print(sms_notif.send())


# 5. Explaining:
# When send() is called, Python checks the specific object first
# So general_notif uses Notification.send() because it's a base Notification object.
# And email_notif and sms_notif call their own send() methods



# ========== Part G - Override and still use the base method =========

# 1 - 4
class Report:
    def __init__(self, title):
        self.title = title

    def get_summary(self):
        return f"Report: {self.title}"

class SalesReport(Report):
    def __init__(self, title, total_sales):
        super().__init__(title)
        self.total_sales = total_sales

    def get_summary(self):
        return super().get_summary() + f", Total Sales: ${self.total_sales}"

quarterly_report = SalesReport("Q3 Performance", 150000)

print(f"\n-------- REPORT SUMMARY ----------")
print(quarterly_report.get_summary())



# ========== Part H - Applied challenge: User accounts ===============

# 1-9 Users challenge
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
        print(f"Welcome, {self.title} {self.username}!")

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


# 10. Explain why AdminUser and PremiumUser have an "is-a" relationship with User
# Admin and Premium users IS-A specific type of User. 
# They inherit all from an User and can extend User with own features