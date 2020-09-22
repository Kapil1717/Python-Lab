#121910313016

def linear(arr , x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
n = int(input("Enter the length of the array:"))
arr = [None]*n
print("Enter the elements")
for i in range(n):
    arr[i] = int(input())
x = int(input("Enter the element to search:"))
print('Element found at '+ str(linear(arr , x)))
