class calculator:
    def __init__(self,num):
        self.num=num
        
    def square(self):
        print(f"the square of {self.num} is {self.num**2}")
        
        
    def squareroot(self):
        print(f"the squareroot of {self.num} is {self.num**0.5}")
        
        
    def cube(self):
            print(f"the cube of {self.num} is {self.num**3}")    
            
    @staticmethod
    def greet():
        print("hello")  
            
abhiyan=calculator(4)
abhiyan.greet()
abhiyan.square()
abhiyan.squareroot()
abhiyan.cube()
