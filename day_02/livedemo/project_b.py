# Project B

# Get several numbers from the user
# Extract the maximum, minimum and all the prime numbers
# in the input
from prime import checkprime
print("project_b.py -> ", __name__)

# input

N = []
print("Enter your numbers: ")
while True:
    n = input("--> ")
    if(n == "!"):
        break
    else:
        if(n.isdigit()):
            N.append(int(n))

# process

primes = []
for n in N:
    if(checkprime(n)):
        primes.append(n)

# output
print("-" * 50)
print(N)
print("MAXIMUM  : ", max(N))
print("MINIMUM  : ", min(N))
print("PRIMES   : ", primes)


