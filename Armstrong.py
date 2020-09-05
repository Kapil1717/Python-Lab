#121910313016

#Taking input from the user
n=int(input("Enter a number:"))
x=n
y=n
sum = 0
sum1 = 0
rem = 0
rem1 = 0

#Logic for sum of the digits
while(x>0):
   rem = x%10
   sum = sum + rem
   x = x//10

#Logic for the sum of the cubes of the digits
while(y>0):
   rem1 = y%10
   sum1 = sum1 + rem1**3
   y = y//10

#Printing the result
print("Sum of digits in the number is : ",sum)
print("Sum of cubes of digits of the number : ",sum1)

#Checking whether the number is armstrong or not
if(sum1==n):
    print(n," is an Armstrong number")
else:
    print(n," is not an Armstrong number")
