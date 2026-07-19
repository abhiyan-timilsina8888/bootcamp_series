class vloger:       # base class
    spot="pokhara"
    def treaking(self):
        print(f"the spot for treaking is {self.spot}")

        
class addspot(vloger):    #derived class or child class
    spot="kathmandu"
    def holiday(self):
        print(f"the spot for holiday is kathmandu")  
    def treaking(self):         # we can overwrite in the child class
        print(f"the spot for treaking is {self.spot}")      
        
        
v=vloger()
v.treaking()


a=addspot()
v.treaking()
a.holiday()
print(v.spot) 
print(a.spot)           
