def selection(arr):
    for i in range(len(arr)-1):
        k=i     #ith element is assumed to the smallest
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[k]):
                k=j
        if(k!=i):
            temp = arr[k]
            arr[k] = arr[i]
            arr[i] = temp
a = list(map(int,input("Enter the elements: ").split()))
selection(a)
print("Elements after selection sort is : ",a)