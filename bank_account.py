class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)


# Create account
account = BankAccount("Sandhya", 5000)

# Display initial balance
account.display_balance()

# Deposit
account.deposit(2000)

# Display balance
account.display_balance()

# Withdraw
account.withdraw(1500)

# Display final balance
account.display_balance()