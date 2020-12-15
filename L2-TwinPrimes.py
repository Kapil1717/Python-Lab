#121910313016
#Printing Twin Primes up to a specified range
def prime(n):           #Fuction1
    isprime=True
    for i in range(2,n):
        if(n%i==0):
            isprime = False
            break
    return isprime
def twin(a,b):          #Function2
    for j in range(a,b+1):
        k = j + 2
        if (prime (j) and prime (k)) :
            print ( {j, k} )

#Taking input from the user
x=int(input("Enter starting value:"))
y=int(input("Enter Ending value:"))
#Calling Function2
twin(x,y)
