class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Constructor called for {self.name}")

    def __del__(self):
        print(f"Destructor called for {self.name}")


# Creating instances of MyClass
obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")
obj3 = MyClass("Object 3")

# Deleting instances
del obj1
del obj2
del obj3
