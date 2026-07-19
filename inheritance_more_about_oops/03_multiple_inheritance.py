class freelancer:
    company="fiverr"
    level=0
    
    def upgradelevel(self):
        self.level= self.level + 1
        print(f"the current level of the employee is {self.level} ")
        
        
class programmer:
    programmer1="abhiyan"
    ecode=111
    company="microsoft"
    
    
class callprogram(programmer,freelancer):
        name="timilsina"
        
        
        
c= callprogram()

print(c.programmer1)
print(c.company)
c.upgradelevel()
        
   
   
    
 
    
    
    
        
               