#121910313016
List = []
n = int(input("Enter the size of the array: "))
print("Enter the elements: ")
for i in range(n):
    x = int(input())
    List.append(x)
if(n==1):
    print("Size should be greater than 1!")
else:
    List.sort()
    print("Second least element is : ",List[1])
