diction ={
     "tero tauko": "your head",
     "kapal":"hair",
     "aalu":"potato"
}
print("options are",diction.keys())
a=input("enter the word \n")

# print("the meaning of the word is :",diction[a])  #it gives the error if the word inputed is not in the dictionary

# it doesnot gives an error if the iputed word is not in the dictionary i.e gives none
print("the meaning of the word is :",diction.get(a))