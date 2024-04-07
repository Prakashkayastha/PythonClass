class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def findArea(self):
        area = self.length * self.breadth
        print(f"The area of the rectangle is : {area}")

    def findPerimeter(self):
        peri = 0.5 * (self.length + self.breadth)
        print(f"The perimeter of the rectangle is : {peri}")

print("Enter the length and breadth of the rectangle:")
length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth:"))
r1=Rectangle(length,breadth)
r1.findArea()
r1.findPerimeter()