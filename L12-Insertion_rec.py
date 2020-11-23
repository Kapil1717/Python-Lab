#121910313016
def InsertionSort(A, i, n): 
    value = A[i]
    j = i
    while j > 0 and A[j - 1] > value:
        A[j] = A[j - 1]
        j = j - 1 
    A[j] = value
 
    if i + 1 < n:
        InsertionSort(A, i + 1, n)
 
arr = list(map(int,input("Enter the Elements: ").split())) 
InsertionSort(arr, 0, len(arr)) 
print(arr)

 
