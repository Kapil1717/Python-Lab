#121910313016
def selectionSort(A, i, n):
    min = i
    for j in range(i + 1, n):        
        if A[j] < A[min]:
            min = j
    if(min!=i): 
        temp = A[i]
        A[i] = A[min]
        A[min] = temp  
 
    if i + 1 < n:
        selectionSort(A, i + 1, n)
 
A = list(map(int,input("Enter the Elements: ").split())) 
selectionSort(A, 0, len(A)) 
print(A)
