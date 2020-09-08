#121910313016

#To Delete the duplicate files in an array
def Remove(arr):
    Final = []
    for i in arr:
        if i not in Final:
         Final.append(i)
    return Final

#Taking inputs from the user
n = int(input("Enter size of the array : "))
a=[None] * n
print("Enter the elements of the array : ")
for i in range(0,n):
    a[i] = int(input())

#Printing original array
print("Original array is :")
print(a)

#Printing the array without duplicate elements
print("Array after removing duplicate elements is : ")
print(Remove(a))
        
