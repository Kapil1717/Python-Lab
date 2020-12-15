#121910313016

#Taking the elements of the array from the user 
n1 = int(input("Enter the size of an array:"))
#Creating an array
a=[None] * n1
print("Enter the elements of the array : ")
for i in range(0,n1):
    a[i] = int(input()) 
n2 = int(input("Enter the size of another array:"))
#Creating another array with the size n2
b = [None] * n2
for i in range(0,n2):
    b[i] = int(input()) 
c=[]
c=a+b
print("Concatinated array is :",c)
