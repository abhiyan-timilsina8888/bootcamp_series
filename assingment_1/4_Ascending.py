n=input("Enter no. of numbers to enter: ")


num =list(map(int,input("Enter the numbers separating with commas: ").split(',')))

if len(num) !=n:
    print(f"Error, enter {n} numbers only... ")
else:
    num.sort()



print(num)
