def Insertion(arr):
    for i in range(1,len(arr)):
        cur = arr[i]
        k=i-1
        while k>=0 and arr[k]>cur:
            arr[k+1]=arr[k]
            k=k-1
        arr[k+1]=cur
a = list(map(int,input("Enter the elements: ").split()))
Insertion(a)
print("Elements after Insertion sort is : ",a)
