# word histogram

# input

text = input("Enter some text: ")

# process

words = text.lower().split()
WH = {}
for word in words:
    if(word in WH.keys()):
        WH[word] = WH[word] + 1
    else:
        WH[word] = 1

# output

print('-'*50)
print(WH)
print('-'*50)

'''
for word, count in WH.items():
    print(word.ljust(8), '|', count)

'''

for key in sorted(WH.keys()):
    print(key, ' --> ', WH[key])

    
