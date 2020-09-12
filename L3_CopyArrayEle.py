#121901313016
n = int(input("Enter size of the array :"))
a=[None]*n    #creating a array
for i in range(0,n):
    a.append(int(input("Enter element:")))
    
print("Original array: ",a)    #Original array
b=[None]*len(a)
l=len(a)
for i in range(0,l):
    b[i]=a[i]
    
for i in range(0,len(b)):
    print(l2[i])
    
print("New array is",b)        #new array
