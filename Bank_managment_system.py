# Base Class (Parent)
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"${amount:.2f} deposited. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}"
        else:
            return "Error: Insufficient funds!"


# Derived Class (Child) for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate=0.02):
        # Inherit holder and balance from BankAccount
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    # Unique method for Savings Account
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest of ${interest:.2f} applied. New balance: ${self.balance:.2f}"


# Derived Class (Child) for Checking Account
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance, transaction_fee=1.50):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee

    # Overriding the withdraw method to include a transaction fee
    def withdraw(self, amount):
        total_cost = amount + self.transaction_fee
        if total_cost <= self.balance:
            self.balance -= total_cost
            return f"${amount:.2f} withdrawn (Fee: ${self.transaction_fee:.2f}). New balance: ${self.balance:.2f}"
        else:
            return f"Error: Insufficient funds to cover withdrawal and fee of ${self.transaction_fee:.2f}!"


# --- Running the Bank System ---

print("--- Testing Savings Account ---")
savings = SavingsAccount("Alice", balance=1000.00)
print(savings.deposit(500.00))      # Inherited method
print(savings.apply_interest())     # Unique Savings method

print("\n--- Testing Checking Account ---")
checking = CheckingAccount("Bob", balance=500.00)
print(checking.deposit(100.00))     # Inherited method
print(checking.withdraw(50.00))     # Overridden method (charges fee)