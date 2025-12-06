# Bank Account Class that allows deposits, withdrawals, and balance inquiries.
class BankAccount:
    
    def __init__(self, initial_balance: float =  0.0):
        self.balance = initial_balance

# Add money to the account. Raise ValueError for negative amounts.         
    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

# Withdraw money from the account. Raise ValueError for negative amounts or insufficient funds.
    def withdraw(self, amount: float) -> bool: 
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            self.balance -= amount
            return True
        return False

# Get the current balance of the account.
    def display_balance(self) -> None:
        print(f"Current balance: ${self.balance:.2f}")
        