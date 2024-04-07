import myModule as m

while True:
    print("1.For GCD")
    print("2.For LCM")
    print("3.For sqrt")
    print("4.For swapping any two number")
    print("5.For Exit")

    choice = int(input("Enter your choice:"))
    if(choice == 1):
        print("Enter two number to find the gcd:")
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        ans=m.findGCD(a,b)
        print(ans)
    elif choice == 2:
        print("Enter two number to find the lcm:")
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        ans=m.findLCM(a,b)
        print(a*b // ans)
    elif choice == 3:
        print("Enter the number to find the square root:")
        a=int(input("Enter the number:"))
        m.findsq(a)
    elif choice == 4:
        print("Enter two number to swap the number:")
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        m.swap(a,b)
    elif choice == 5:
        print("Exit")
        break
    else:
        print("Invalid choice,please enter a valid choice")


