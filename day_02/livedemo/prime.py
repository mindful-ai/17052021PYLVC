# Program to determine if a number is prime or not

def checkprime(n):
    for x in range(2, n):
        if(n % x == 0):
            return False
    return True

print("prime.py -> ", __name__)
    
if __name__ == "__main__":
    
    n = int(input("Enter a number: "))
    if(checkprime(n)):
        print("The number is prime")
    else:
        print("The number is  not prime")

