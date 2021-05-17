# Program to specify if the difference is positive
# negative or zero
# if the result is positive then print if the result is even or odd

# input
a = int(input("Enter value for a :"))
b = int(input("Enter value for b :"))

# process
res = a - b

# output
if (res > 0):
    if(5 <= res <= 10):
        print("The result is between 5 and 10")
    else:
        print("The result is above 10")
    print("The result is positive")
elif (res < 0):
    print("The result is negative")
else:
    print("The result is zero")
    
