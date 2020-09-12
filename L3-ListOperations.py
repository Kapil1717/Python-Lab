#121910313016

choice=int(input("Enter a number for an operation on list:"))

if(choice==1):
  #Taking the elements of the array from the user 
  n1 = int(input("Enter the size of the original array:"))
  a=[None] * n1
  print("Enter the elements of the array : ")
  for i in range(0,n1):
      a[i] = int(input()) 
  #Creating another array with the size of first array
  b = [None] * n1
  #Copying all the elements from a to b
  for i in range(0,n1):
      b[i] = a[i]
  #Displaying the elements of the original array
  print("Elements of the original array is :")
  print(a)
  #Displaying the elements of the duplicate array
  print("Elements of the duplicate array is :")
  print(b)

elif(choice==2):
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

elif(choice==3):
    a = []  # creating an array
    n = int(input("Enter array size: ))
    for i in range ( , n) :
        l1.append ( int ( input ( "Enter element:" ) ) )
    print (a)
    z = int ( input ( "Enter index of the elemnts to be removed:" ) )
    a.pop (z)
    print (a)
    
 elif(choice==4):
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
    
elif(choice==5):
    a = []  # creating an array
    n = int ( input ( "Enter array size:" ) )
    for i in range (0 , n) :
        a[i] =  int ( input ( "Enter an element : " ) ) 
    print ( "array:",a )
else:
    print(" Please enter a correct choice! ")
    
  
    
