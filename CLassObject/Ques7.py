class Shape:
    def findVolume(self):
        pass

class Box(Shape):
    def __init__(self,length,breadth,height):
        self.length=length
        self.breadth=breadth
        self.height=height

    def findVolume(self):
        return self.length*self.breadth*self.height

length = float(input("Enter length of the box: "))
width = float(input("Enter width of the box: "))
height = float(input("Enter height of the box: "))

box=Box(length,width,height)
print("Volume of the Box: ",box.findVolume())