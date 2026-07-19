class employee:
    company="google"


    @staticmethod
    def greet():
       print("hello abhiyan")   
    

    def __init__(self, name , salary):
        self.name = name
        self.salary= salary



    def getsalary(self,signature):
        print(f"salary of {self.name} working in {self.company} is {self.salary}")
        print(signature)


name= input("enter your name:\n")
salary= int(input("enter your salary:\n"))     


a=employee(name,salary)
a.greet()  

a.getsalary('Done')  #<<<<<employee.getsalary(a)

    



   



