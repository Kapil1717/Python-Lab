#121910313016
def displayMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")            
        print()
    

#Function to convert matrix into sparse matrix
def convertToSparseMatrix(matrix):
    #Creating an empty sparse matrix list
    sparseMatrix=[]

    #Searching values greater than zero
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            if matrix[i][j]!=0:
                temp = []                   #Creating a temporary sublist
                temp.append(i)              #Appending row , column values ,element into the sublist
                temp.append(j)
                temp.append(matrix[i][j])
                sparseMatrix.append(temp)   #Appeding the sublist into the sparse matrix list

    print("\nSparse Matrix : ")
    displayMatrix(sparseMatrix)             #Displaying the sparse matrix

normalMatrix = [[1,0,0,0],
                [0,2,0,0],
                [0,0,3,0],
                [0,0,0,4]]

displayMatrix(normalMatrix)                 #Displaying the matrix

convertToSparseMatrix(normalMatrix)         #Converting the matrix into sparse matrix
    
