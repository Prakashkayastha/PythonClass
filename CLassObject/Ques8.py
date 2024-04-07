class Box:
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height

    def Volume(self):
        return self.length * self.width*self.height

class Cost(Box):
    def __init__(self,length,width,height,cost_per_unit):
        Box.__init__(self,length,width,height)
        self.cost_per_unit=cost_per_unit
    def calculate_cost(self):
        return self.Volume() * self.cost_per_unit

class Weight(Cost):
    def __init__(self,length,width,height,cost_per_unit,weight_per_unit):
        Cost.__init__(self,length,width,height,cost_per_unit)
        self.weight_per_unit=weight_per_unit
    
    def calculate_weight(self):
        return self.Volume() * self.cost_per_unit


length = float(input("Enter length of the box: "))
width = float(input("Enter width of the box: "))
height = float(input("Enter height of the box: "))
cost_per_unit = float(input("Enter cost per unit volume: "))
weight_per_unit = float(input("Enter weight per unit volume: "))
box= Weight(length,width,height,cost_per_unit,weight_per_unit)
print("Volume of the Box: ",box.Volume())
print("Cost of the Box: ",box.calculate_cost())
print("Weight of the Box: ",box.calculate_weight())