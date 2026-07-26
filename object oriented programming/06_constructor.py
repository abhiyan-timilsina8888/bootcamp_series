class employee:
    def __init__(self,name,salary,passion):
         self.name=name
         self.salary=salary
         self.passion=passion   
         print("employee is created\n")
        
    def getdetails(self):
        print(f"the name of the worker is {self.name}")
        print(f"the salary of the worker is {self.salary}")
        print(f"the passion of the worker is {self.passion}")
       
abhiyan=employee("abhiyan",10000000,"coding")
abhiyan.getdetails()

