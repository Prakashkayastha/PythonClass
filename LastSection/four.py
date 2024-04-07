class ATM:
    def __init__(self):
        self.users = []

    def generate_account_number(self):
        if len(self.users) == 0:
            return 1001
        else:
            return self.users[-1]['account_number'] + 1

    def create_account(self, name, mobile_no, pin, initial_balance):
        account_number = self.generate_account_number()
        account = {'account_number': account_number, 'name': name, 'mobile_no': mobile_no, 'pin': pin, 'balance': initial_balance}
        self.users.append(account)
        print(f"Account created successfully! Account number: {account_number}")

    def verify_user(self, account_number, pin):
        for user in self.users:
            if user['account_number'] == account_number and user['pin'] == pin:
                return user
        return None

class Banking(ATM):
    def __init__(self):
        super().__init__()

    def withdraw(self, user, amount):
        if user['balance'] >= amount:
            user['balance'] -= amount
            print(f"Withdrawal successful. Updated balance: {user['balance']}")
        else:
            print("Insufficient funds.")

    def fast_withdraw(self, user, amount):
        if user['balance'] >= amount:
            user['balance'] -= amount
            print(f"Withdrawal of {amount} successful. Updated balance: {user['balance']}")
        else:
            print("Insufficient funds.")

    def change_pin(self, user, new_pin):
        user['pin'] = new_pin
        print("PIN changed successfully.")

    def check_balance(self, user):
        print(f"Current balance: {user['balance']}")


# Creating a new ATM object
banking = Banking()

# Creating new accounts
banking.create_account("John", "1234567890", 1234, 5000)
banking.create_account("Alice", "9876543210", 4321, 7000)

# User login
account_number = int(input("Enter your account number: "))
pin = int(input("Enter your PIN: "))

user = banking.verify_user(account_number, pin)
if user:
    print("Login successful.")
    option = input("Choose an option:\n1. Withdraw\n2. Fast Withdraw\n3. Change PIN\n4. Check Balance\nEnter option number: ")
    if option == '1':
        amount = float(input("Enter the amount to withdraw: "))
        banking.withdraw(user, amount)
    elif option == '2':
        amount = float(input("Choose an option:\n1. 500\n2. 1000\n3. 2000\n4. 5000\nEnter option number: "))
        if amount == 1:
            banking.fast_withdraw(user, 500)
        elif amount == 2:
            banking.fast_withdraw(user, 1000)
        elif amount == 3:
            banking.fast_withdraw(user, 2000)
        elif amount == 4:
            banking.fast_withdraw(user, 5000)
        else:
            print("Invalid option.")
    elif option == '3':
        new_pin = int(input("Enter new PIN: "))
        banking.change_pin(user, new_pin)
    elif option == '4':
        banking.check_balance(user)
    else:
        print("Invalid option.")
else:
    print("Invalid account number or PIN.")
