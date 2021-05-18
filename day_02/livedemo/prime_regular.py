# Program to determine if a number is prime or not

n = int(input("Enter a number: "))

prime = True

for x in range(2, n):
    if(n % x == 0):
        prime = False
        break

if(prime == True):
    print("Then number is prime")
else:
    print("The number is not prime")

    
