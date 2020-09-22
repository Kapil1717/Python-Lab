#121910313016
def binary(arr , l , h , x):
    if h >= l :
        mid = (h+l)//2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary(arr , l , mid-1 , x)

        else :
            return binary(arr , mid+1 , h , x)
    else :
        return -1
        
n = int(input('Enter the length of the array: '))
a = [None]*n

print("Enter the elements of the array: ")
for i in range(n):
    a[i] = int(input())
    
x = int(input('Enter the element to search: '))

result = binary(a , 0 ,len(a)-1 , x)

if result != -1:
    print('Element is present at index ',result)
else:
    print('Element is not present in the array')
        
