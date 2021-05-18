N = [1, 2, 3, 4, 5]

un = int(input("Enter a number: "))

for n in N:
    if(un % n != 0):
        print("Failed")
        break
else:
    print("Passed")
