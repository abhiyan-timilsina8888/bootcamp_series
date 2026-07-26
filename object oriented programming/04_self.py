class employee:
    company="google"
    

    def __init__(self,name,salary):
        self.name =name
        self.salary= salary

    
    def getsalary(self):
        print(f"salary of {self.name} working in {self.company} is {self.salary}")


name= input("enter your name:\n")
salary= int(input("enter your salary:\n"))       
        
a=employee(name,salary)


a.getsalary()  #<<<<<employee.getsalary(a)



        