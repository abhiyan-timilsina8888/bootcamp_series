row1= int(input("enter the rows of first matrix:"))
col1= int(input("enter the columns of first matrix:"))


x=[]


print("enter the first matrix:")
for i in range(row1):
    x.append(list(map(int,input().split())))



row2= int(input("enter the rows of second matrix:"))
col2= int(input("enter the columns of second matrix:"))


y=[]


print("enter the second matrix: ")
for i in range(row2):
    y.append(list(map(int,input().split())))



if col1  != row2 :
    print("Matrix multiplication is not possible.")


else:
    mat=[[sum(x[i][k] * y[k][j] for k in range(col1))
               for j in range(col2)]
               for i in range(row1)]

    print("Result:")
    for row in mat:
        print(row)