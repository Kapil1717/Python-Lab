def mergeSort(myList):
    if len(myList)>1 :
        mid = len(myList)//2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i<len(left) and j<len(right) :
            if left[i] < right[j]:
                myList[k] = left[i]
                i=i+1
                k=k+1
            else:
                myList[k] = right[j]
                j=j+1
                k=k+1
        while i < len(left):
            myList[k] = left[i]
            i=i+1
            k=k+1
        while j < len(right):
            myList[k] = right[j]
            j=j+1
            k=k+1
a = list(map(int,input("Enter the elements: ").split()))
mergeSort(a)
print("Elements after Merge sort is : ",a)
