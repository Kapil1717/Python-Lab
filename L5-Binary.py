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
a = [1,17,18,45,77]
x = 18

result = binary(a , 0 ,len(a)-1 , x)

if result != -1:
    print('Element is present at index ',result)
else:
    print('Element is not present in the array')
        
