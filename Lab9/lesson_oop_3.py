# ========== Part A - Polymorphism ===============================

# 1 - 2. Create three classes with send()
class EmailNotification:
    def send(self):
        return "Sending email notification to user..."


class SMSNotification:
    def send(self):
        return "Sending SMS notification to phone..."


class PushNotification:
    def send(self):
        return "Sending push notification to device screen..."


# 3. Create one object from each class and store them in the same list
notifications = [EmailNotification(), SMSNotification(), PushNotification()]

# 4. Loop through the list and call send() on every object
print("-------- POLYMORPHISM DEMO ----------")
for notification in notifications:
    print(notification.send())


# 5. Explanation:
# The loop doesn't need to know the exact class of each object because of polymorphism: while every object has
# send() method, Python will execute the correct send() for that specific object



# ============= Part F - __str__ with inheritance =================

# 1 - 2. Create a base class Account with owner and balance and Add __str__ to Account
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"

# 3 - 4. SavingsAccount(Account), override __str__ 
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return (f"{super().__str__()}, Interest rate: {self.interest_rate}")

simple_account = Account('Kid', 200)
saving_account = SavingsAccount('Alex', 30000, 2)
print("\n--------- ACCOUNTS COMPARING --------")
print("Simple account: ", simple_account)
print("Saving account: ", saving_account)



# ============ Part H - Applied challenge: Export system ================

# 1 - 6
class Exporter:
    def export(self, data):
        return f"Exporting data: {data}"

    def __str__(self):
        return "Base Exporter"


class ConsoleExporter(Exporter):
    def export(self, data):
        return f"[CONSOLE OUTPUT] -> {data}"

    def __str__(self):
        return "Console Exporter"


class TextExporter(Exporter):
    def export(self, data):
        return f"[TEXT FILE] Saving line: '{data}'"

    def __str__(self):
        return "Text Exporter"


class SummaryExporter(Exporter):
    def export(self, data):
        words_count = len(str(data).split())
        return f"[SUMMARY] Data contains {words_count} words. Content: {data}"

    def __str__(self):
        return "Summary Exporter"


exporters_list = [
    ConsoleExporter(),
    TextExporter(),
    SummaryExporter()
]


# 7. Loop through the list and call export()
sample_data = "User is logged in"

print("\n---- EXPORT SYSTEM POLYMORPHISM -------")
for exporter in exporters_list:
    print(f"Using {exporter}:")
    print(exporter.export(sample_data))
    print()


# 8. Create an independent class (not inheriting from Exporter) with export() method (Duck Typing)
class DatabaseLogger:
    def __init__(self, db_name):
        self.db_name = db_name

    def export(self, data):
        return f"[DATABASE: {self.db_name}] Data: '{data}'"

    def __str__(self):
        return f"Database Logger ({self.db_name})"


db_logger = DatabaseLogger("production_db")
exporters_list.append(db_logger)

print("------ DUCK TYPING DEMO ----------------")
for exporter in exporters_list:
    print(exporter.export(sample_data))


# 9. Use isinstance() to inspect type relationship
print("\n------ ISINSTANCE CHECK ------------")
text_exp = TextExporter()

print(f"Is text_exp an instance of TextExporter? {isinstance(text_exp, TextExporter)}")
print(f"Is text_exp an instance of Exporter? {isinstance(text_exp, Exporter)}")
print(f"Is db_logger an instance of Exporter? {isinstance(db_logger, Exporter)}")


# 10. Example of composition (HAS-A relationship)
class DataManager:
    def __init__(self, exporter):
        self.exporter = exporter 

    def process_and_export(self, data):
        cleaned_data = str(data).strip()
        return self.exporter.export(cleaned_data)

# DataManager HAS-A Exporter.
# DataManager is not an Exporter, but it HAS An Exporter object inside