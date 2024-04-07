class Bank:
    def __init__(self):
        self.accounts = []

    def generate_account_number(self):
        if len(self.accounts) == 0:
            return 1001
        else:
            return self.accounts[-1]['account_number'] + 1

    def create_account(self, name, mobile_no, initial_balance):
        account_number = self.generate_account_number()
        account = {'account_number': account_number, 'name': name, 'mobile_no': mobile_no, 'balance': 3000 + initial_balance}
        self.accounts.append(account)
        print(f"Account created successfully! Account number: {account_number}")

class Transaction(Bank):
    def __init__(self):
        super().__init__()

    def deposit(self, account_number, amount):
        for account in self.accounts:
            if account['account_number'] == account_number:
                account['balance'] += amount
                print(f"Amount {amount} deposited successfully. Updated balance: {account['balance']}")
                break
        else:
            print("Account number not found.")

    def withdraw(self, account_number, amount):
        for account in self.accounts:
            if account['account_number'] == account_number:
                if account['balance'] >= amount:
                    account['balance'] -= amount
                    print(f"Amount {amount} withdrawn successfully. Updated balance: {account['balance']}")
                else:
                    print("Insufficient funds.")
                break
        else:
            print("Account number not found.")

    def check_balance(self, account_number):
        for account in self.accounts:
            if account['account_number'] == account_number:
                print(f"Current balance: {account['balance']}")
                break
        else:
            print("Account number not found.")

# Creating a new bank object
bank = Transaction()

# Creating new accounts
bank.create_account("John", "1234567890", 5000)
bank.create_account("Alice", "9876543210", 7000)

# Depositing money
bank.deposit(1001, 2000)

# Withdrawing money
bank.withdraw(1002, 3000)

# Checking balance
bank.check_balance(1001)
