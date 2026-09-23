# ================ Part C - Inheritance fundamentals =============

# 
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