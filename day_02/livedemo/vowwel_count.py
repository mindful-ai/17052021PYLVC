# Extract the number of vowels in a given text

# input

text = input("Enter text: ")

# process

vowels = "aeiou"
DV = {}
for vowel in vowels:
    DV.setdefault(vowel, text.lower().count(vowel))

# ouput

print('-'*50)
print(DV)
print('-'*50)

for k, v in DV.items():
    print(k.ljust(5), '|', v)
    
print("Number of vowels found = ", sum(DV.values()))
