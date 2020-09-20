#121910313016
#Taking input from the user
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
#Creating an empty matrix
matrix = []
for i in range(r):
    a = []
    for j in range (c):
        a.append(int(input()))
    matrix.append(a)
#Displaying the matrix
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
n = int(input("Enter a threshold value:"))
#Creating an empty sparse matrix list
sparseMatrix=[]             
for i in range(len(matrix)):
    for j in range(len(matrix[1])):
        if matrix[i][j]<=n:
            matrix[i][j]=0
        if matrix[i][j]!=0:
            temp=[]         #Creating a temporary sublist
            temp.append(i)
            temp.append(j)
            temp.append(matrix[i][j])
            sparseMatrix.append(temp)
print("\nsparsematrix:")            
for i in sparseMatrix:
    for j in i:
        print(j,end=" ")
    print()
