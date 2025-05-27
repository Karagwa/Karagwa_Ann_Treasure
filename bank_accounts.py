# Bank accounts: Saving account and current account inherit from bank account

# Super class
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")    

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}")
        
        
# Subclass for Savings Account
class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.0):
        super().__init__(account_number, account_holder, balance)
        
        self.interest_rate = interest_rate
        
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)
        print(f"Interest added: ${interest:.2f}. New balance is ${self.balance:.2f}.")
        
        
# Child class for Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit  # Default overdraft limit

    

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
            
            
saving = SavingAccount("123456789", "John Doe", 1000)
current= CurrentAccount("987654321", 500.0, 200.0)

saving.display_balance()
saving.add_interest()
saving.withdraw(200)

current.display_balance()
current.withdraw(600)
            