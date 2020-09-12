#121901313016
x=0
def search(arr):      #Fuction 
    x=int(input("Enter element to search :"))
    for i in arr:
        if(x==i):
            flag=1
            break
        else:
            flag=0
    if(flag==1):
        print("Element ", x ," found in the array at ", i-1)
    else:
        print("Element not found")
        
n=int(input("Enter array size:"))
a=[None]*n            #creating an array

for i in range(0,n):
    a[i] = int(input("Enter element:"))
    
print("array: ",a)
search(a)             #function calling
