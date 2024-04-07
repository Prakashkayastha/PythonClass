import myModule as m
def scientific_calculator():
    print("Welcome to Scientific Calculator!")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (x^y)")
    print("7. Square Root (√)")
    print("8. Cubic Root (³√)")
    print("9. Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("12. Logarithm (log)")
    print("13. Exponential (exp)")
    print("14. Absolute Value (|x|)")
    print("0. Exit")

    while True:
        choice = input("Enter operation number (0-14): ")
        
        if choice == '0':
            print("Exiting...")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                print("Result:", m.add(num1, num2))
            elif choice == '2':
                print("Result:", m.subtract(num1, num2))
            elif choice == '3':
                print("Result:", m.multiply(num1, num2))
            elif choice == '4':
                print("Result:", m.divide(num1, num2))
            elif choice == '5':
                print("Result:", m.modulus(num1, num2))
            elif choice == '6':
                print("Result:", m.power(num1, num2))

        elif choice in ['7', '8', '9', '10', '11', '12', '13', '14']:
            num = float(input("Enter number: "))
            if choice == '7':
                print("Result:", m.sqrt(num))
            elif choice == '8':
                print("Result:", m.cubic_root(num))
            elif choice == '9':
                print("Result:", m.sin(num))
            elif choice == '10':
                print("Result:",m. cos(num))
            elif choice == '11':
                print("Result:", m.tan(num))
            elif choice == '12':
                print("Result:",m.log(num))
            elif choice == '13':
                print("Result:", m.exp(num))
            elif choice == '14':
                print("Result:", m.absolute(num))
        else:
            print("Invalid choice. Please enter a number between 0 and 14.")


scientific_calculator()
