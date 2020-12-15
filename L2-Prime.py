#121910313016

#Taking input from the user
a=int(input("Enter starting limit:"))         #Starting Value
b=int(input("Enter ending limit:"))           #Ending Value

#printing prime numbers up to a given range
print("Prime numbers between the given range are:")

#logic starts here
for num in range(a, b+1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
