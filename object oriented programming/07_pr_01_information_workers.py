class programmer():
    company="microsoft"
    def __init__(self,name, product):
        self.name=name
        self.product=product
        
    def getinfo(self):
        print(f"the name of the employee is {self.name} and the product is {self.product}")    
        
abhiyan=programmer('abhiyan','ms-word')

kevin=programmer('kevin','office')

abhiyan.getinfo()
kevin.getinfo()  