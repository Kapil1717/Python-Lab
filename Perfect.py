#121910313016
#To check whether a number is perfect number or not
sum = 0 
n=int(input("Enter a number:"))
#logic starts here
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
