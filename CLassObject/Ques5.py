class MyClass:
    __count = 0  # Private class variable to count the number of objects

    def __init__(self):
        MyClass.__count += 1  # Increment count each time an object is created

    @classmethod
    def get_count(cls):
        return cls.__count  # Return the count of objects

# Example usage:
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print("Number of objects created:", MyClass.get_count())  # Output: 3
