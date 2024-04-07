class SwapNumbers:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def swapWith3rdvariable(self):
        print(f"Before swapping : a = {self.num1} and b ={self.num2}")
        temp=self.num1
        self.num1=self.num2
        self.num2=temp
        print(f"After swapping : a = {self.num1} and b ={self.num2}")
    def swapwithout3rdvariable(self):
        print(f"Before swapping : a = {self.num1} and b ={self.num2}")
        self.num1=self.num1^self.num2
        self.num2=self.num1^self.num2
        self.num1=self.num1^self.num2
        print(f"After swapping : a = {self.num1} and b ={self.num2}")
    
s1=SwapNumbers(3,5)
s1.swapWith3rdvariable()
s1.swapwithout3rdvariable()