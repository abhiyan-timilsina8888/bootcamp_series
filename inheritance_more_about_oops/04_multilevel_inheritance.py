class person:
    country="nepal"
    def takebreath(self):
        print("i am breathing like always...")
      
class employee(person):
    
    company="iphone"
    a=input("enter the salary")
   
    def salary(self):
        print(f"the salary of the employee is {self.a}")

    def takebreath(self):
        print(f"let's take fresh air..")
      
class programmer(employee):
    company="samsung"
    def salary(self):
         print("as much as you like..")
         
    def takebreath(self):
        print("so much error i fell like not to take a breath...")
        
p=person()
p.takebreath()
print(p.country)

e=employee()
e.salary()
print(e.country)
pr=programmer()
pr.salary()
                   