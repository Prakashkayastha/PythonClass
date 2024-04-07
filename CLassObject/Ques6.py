from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self,principal,rate,time):
        self.principal=principal
        self.time=time
        self.rate=rate
    
    @abstractmethod
    def simple_intrest(self):
        pass
    def compound_intrest(self):
        pass

class SBI(Bank):
    def __init__(self,principal,rate,time):
        super().__init__(principal,rate,time)
    
    def simple_intrest(self):
        return (self.principal * self.rate * self.time)/100
    def compound_intrest(self):
        return self.principal * (1 + self.rate/ 100) ** self.time - self.principal
    
class UBI(Bank):
    def __init__(self,principal,rate,time):
        super().__init__(principal,rate,time)
    def simple_intrest(self):
        return (self.principal * self.rate * self.time) / 100

    def compound_intrest(self):
        return self.principal * (1 + self.rate / 100) ** self.time - self.principal
    
class AXIS(Bank):
    def __init__(self,principal,rate,time):
        super().__init__(principal,rate,time)
    
    def simple_intrest(self):
        return (self.principal * self.rate * self.time) / 100
    
    def compound_intrest(self):
        return self.principal * ( 1 + self.rate/100) ** self.time - self.principal


sbi_account = SBI(1000,5,2)
print("SBI Simple Intrest: ",sbi_account.simple_intrest())
print("SBI Compound Intrest: ",sbi_account.compound_intrest())

ubi_account = UBI(10000, 6, 2)
print("UBI Simple Interest:", ubi_account.simple_intrest())
print("UBI Compound Interest:", ubi_account.compound_intrest())

axis_account = AXIS(10000, 7, 2)
print("AXIS Simple Interest:", axis_account.simple_intrest())
print("AXIS Compound Interest:", axis_account.compound_intrest())


    