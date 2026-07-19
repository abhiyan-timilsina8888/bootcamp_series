class person:
    country="nepal"
    def takebreath(self):
        print("i am breathing like always...")
      
class employee(person):
    
    company="iphone"
   
   
    def salary(self):
        print(f"the salary of the employee is {self.salary}")

    def takebreath(self):
        super().takebreath()
        print(f"let's take fresh air..")
      
class programmer(employee):
    company="samsung"
    def salary(self):
         print("as much as you like..")
         
    def takebreath(self):
        super().takebreath()
        print("so much error i fell like not to take a breath...")
        
p=person()
p.takebreath()

e=employee()
e.takebreath()

pr=programmer()
pr.takebreath()
                   