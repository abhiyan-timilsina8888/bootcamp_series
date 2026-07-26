favlang={}
a=input("enter your favourite language abhiyan \n")
b=input("enter your favourite language avenjal \n")
c=input("enter your favourite language yushup \n")
d=input("enter your favourite language arzuu \n")
favlang['abhiyan']=a
favlang['avenjal']=b 
# favlang['yushup']=c 
favlang['abhiyan']=c  # case for having two name same gives the latest value to the key
favlang['arzuu']=d 
print(favlang)
