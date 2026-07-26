num= input("Enter the number\n") 

# Here we don't use int method cause [::-1] only works for string.


a= num[::-1]

if num==a:
    print(f"{num} is Palindrome")
    
else:
    print(f"{num} is not a Palindrome")
