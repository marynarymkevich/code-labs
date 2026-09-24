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
print("--------- ACCOUNTS COMPARING --------")
print("Simple account: ", simple_account)
print("Saving account: ", saving_account)



# ============ Part H - Applied challenge: Export system ================

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