import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def cubic_root(x):
    return x ** (1/3)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x):
    return math.log10(x)

def exp(x):
    return math.exp(x)

def absolute(x):
    return abs(x)