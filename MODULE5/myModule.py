def deposit(amount,balance):
    balance = balance + amount
    return balance

def withdraw(amount,balance):
   
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
        if(balance < 3000):
            print("Please maintain a minimum balance of Rs 3000")
        return balance
    else:
        print("Insufficient funds.")

def checkbalance(balance):
    print(f"The balance in the account is : {balance}")