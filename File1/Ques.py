import math

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# a) Create a file number.txt and store 3 user defined numbers joined using ‘,’
numbers = input("Enter three numbers separated by commas: ")
with open("number.txt", "w") as file:
    file.write(numbers)

# b) Read the content of number.txt file as a string file and split them into 3 numbers.
# Then find factorial of difference between largest and smallest among 3 numbers.
with open("number.txt", "r") as file:
    data = file.read()
    numbers = list(map(int, data.split(',')))

min_num = min(numbers)
max_num = max(numbers)
diff = max_num - min_num
fact_diff = factorial(diff)

# Finally append the factorial as factorial=obtained factorial in number.txt
with open("number.txt", "a") as file:
    file.write(f"\nfactorial={fact_diff}")

# c) Rename the file as fact.txt in python
import os
os.rename("number.txt", "fact.txt")

print("Factorial of the difference:", fact_diff)
print("File renamed to fact.txt")
