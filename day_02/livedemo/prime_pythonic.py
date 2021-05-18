# Program to determine if a number is prime or not

n = int(input("Enter a number: "))

for x in range(2, n):
    if(n % x == 0):
        print("The number is not prime")
        break
else:
    print("Then number is prime")
