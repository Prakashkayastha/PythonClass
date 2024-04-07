class Triangle:
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3

    def findArea(self):
        ans=0.5*self.side1*self.side2
        print(f"Thre area of the triangle is : {ans}")
    
    def findPerimeter(self):
        perimeter=self.side1 + self.side2 + self.side3
        print(f"The perimeter of the triangle is : {perimeter}")

print("Enter the three sides of the triangle:")
side1=int(input("Enter 1st one:"))
side2=int(input("Enter 2nd one:"))
side3=int(input("Enter last one:"))
t1=Triangle(side1,side2,side3)
t1.findArea()
t1.findPerimeter()