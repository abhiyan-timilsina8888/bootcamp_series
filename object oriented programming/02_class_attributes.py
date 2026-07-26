class employee:
    company="google"
    
abhiyan=employee()
naruto=employee()


print("before changing:",abhiyan.company)   
print("before changing:",naruto.company) 


employee.company="youtube"
print("after changing:",abhiyan.company)   
print("after changing:",naruto.company) 