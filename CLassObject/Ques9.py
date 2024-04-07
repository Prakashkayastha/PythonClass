from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self,side):
        self.side=side
        
    def area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side

# Creating instances of Rectangle and Square
rectangle = Rectangle(5, 4)
square = Square(5)

# Calculating and printing area and perimeter for rectangle
print("Rectangle:")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

# Calculating and printing area and perimeter for square
print("\nSquare:")
print("Area:", square.area())
print("Perimeter:", square.perimeter())
