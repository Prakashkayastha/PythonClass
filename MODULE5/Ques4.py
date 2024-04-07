import myModule as m
balance=int(input("Enter a fixed value to assign balance for account (greater than 3000):"))
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice =int(input("Ente your choice:"))

    if choice == 1:
            amount = float(input("Enter the amount to deposit: "))
            balance =m.deposit(amount,balance)
            print(f"Deposit successful,Total balance = {balance}")
    elif choice == 2:
            amount = float(input("Enter the amount to withdraw: "))
            balance = m.withdraw(amount,balance)
            print(f"Withdraw successful,remaining balance = {balance}")
    elif choice == 3:
            m.checkbalance()
    elif choice == 4:
            print("Thank you for banking with us!")
            break
    else:
            print("Invalid choice. Please try again.")


