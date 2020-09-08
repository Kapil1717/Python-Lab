#121910313016

#Taking the elements of the array from the user 
n1 = int(input("Enter the size of the original array:"))
a=[None] * n1
print("Enter the elements of the array : ")
for i in range(0,n1):
    a[i] = int(input()) 


#Creating another array with the size of first array
b = [None] * n1


#Copying all the elements from a to b in reverse order
for i in range(0,n1):
    b[i] = a[n1-i-1]

#Displaying the elements of the original array
print("Elements of the original array is :")
print(a)

#Displaying the elements of the duplicate array
print("Elements of the duplicate array is :")
print(b)
    
