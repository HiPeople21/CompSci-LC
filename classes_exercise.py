class BankAccount:
    def __init__(self, balance: float = 0) -> None:
        self.balance = balance
        
    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("You must deposit a positive amount of money.")
            return False
        self.balance += amount
        return True
        
    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("You must withdraw a positive amount of money.")
            return False
        if amount > self.balance:
            print("Insufficient funds in account.")
            return False
        self.balance -= amount
        return True
    
    def get_balance(self) -> float:
        return self.balance
    
    def transfer(self, amount: float, other_account: "BankAccount") -> bool:
        if self.withdraw(amount):
            other_account.deposit(amount)
        
    def __str__(self) -> str:
        return f"Bank Account: ${self.balance}"
    
    
bank_account_a = BankAccount(100)
bank_account_b = BankAccount()

print(bank_account_a)
print(bank_account_b)

# Demonstrates depositing
bank_account_a.deposit(50)  # Works fine
bank_account_b.deposit(-50)  # Gives error

print(bank_account_a)
print(bank_account_b)

# Demonstrates withdrawing
bank_account_a.withdraw(50)  # Works fine
bank_account_b.withdraw(1)  # Gives error
bank_account_b.withdraw(-1)  # Gives error

print(bank_account_a)
print(bank_account_b)

# Demonstrates transferring
bank_account_a.transfer(50, bank_account_b)  # Works fine
bank_account_a.transfer(100000, bank_account_b)  # Gives error
bank_account_a.transfer(-1, bank_account_b)  # Gives error

print(bank_account_a)
print(bank_account_b)