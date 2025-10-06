class BankAccount:
    def __init__(self):
        self.balance = 0
        self.deposit(0)
        self.withdraw(0)
        self.display_balance()


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(f"Current balance: {self.balance}")