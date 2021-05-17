# Accept 10 numbers from the user
# Separate the odd and even numbers

import random

# input

# print("Enter 10 numbers one by one:")
print("100 Random Numbers")
num = []

'''
for i in range(10):
    n = int(input("# => "))
    num.append(n)
'''

for i in range(100):
    num.append(random.randint(1,100))
    
# process

odds = []
evens = []
for n in num:
    if(n % 2 == 0):
        evens.append(n)
    else:
        odds.append(n)


# output

print("-"*40)
print("ODDS : ", odds)
print("EVENS: ", evens)
