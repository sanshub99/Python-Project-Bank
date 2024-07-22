class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self, entered_pin):
        return entered_pin == self.pin

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal failed."

def main():
    # Sample account details
    account_number = "4971205190"
    pin = "0000"
    initial_balance = 500

    user_account = BankAccount(account_number, pin, initial_balance)

    # Login
    if not user_account.login(input("Enter your PIN: ")):
        print("Incorrect PIN. Exiting...")
        return

    print(f"Login successful for account no {account_number}")

    # Perform transactions
    while True:
        choice = input("\nSelect banking option:\n1. Deposit\n2. Withdraw\n3. Exit\nEnter your choice (1/2/3): ")

        if choice == "1":
            print(user_account.deposit(float(input("Enter the deposit amount: "))))
        elif choice == "2":
            print(user_account.withdraw(float(input("Enter the withdrawal amount: "))))
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
