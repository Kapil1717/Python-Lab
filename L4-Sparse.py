#121910313016
matrix=[[16,0,70,0],
        [17,0,11,0],
        [90,0,18,0],
        [0,45,0,77]]
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
sparseMatrix=[]             #Creating an empty sparse matrix list
for i in range(len(matrix)):
    for j in range(len(matrix[1])):
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
