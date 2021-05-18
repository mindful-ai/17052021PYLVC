# Program to extract the maximum from the array

L = [12, 34, 45, 56, 78, 11, 34]

'''
L.sort()
print("MIN: ", L[0])
print("MAX: ", L[-1])
'''

'''
m = L[0]
for n in L:
    if(n > m):
        m = n
print("MAX: ", m)

m = L[0]
for n in L:
    if(n < m):
        m = n
print("MIN: ", m)
'''

print("MAX: ", max(L))
print("MAX: ", min(L))
