# Design a word jumble game
# L P E P S A
# -> [1] ? 
# -> [Hint] This is a fruit
# -> [2] APPLES
import random

def jumble(w):
    temp = list(w)
    random.shuffle(temp)
    return ''.join(temp)

# Collection of words
L = ["apples", "laptop", "mangoes", "computer", "mobile", "hyundai", "mercedes", "samsung"]
random.shuffle(L)

points = 0

# Repeat until all words are done
# Pick a word
for word in L:

    # Jumble the word
    jword = jumble(word)

    # Show the word to the user
    print("Jumbled Word -> ", jword)

    # Ask for the user input
    uword = input("Your guess ? ")

    # Compare the user input with original word
    # Update points
    if(uword == word):
        points += 1
        print("Correct!")
    else:
        print("Incorrect..")

# Print the results
if(points > 6):
    print("Excellent Playing!")
elif(3 <= points <= 6):
    print("Good")
else:
    print("Improvement needed")
