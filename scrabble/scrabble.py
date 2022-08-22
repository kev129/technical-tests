# Functions required:
# Get score, Get tiles, Randomize bag, Find valid word, Find longest valid word, Find highest scoring word, Find highest scoring word if one of the letters can score triple

# Test case: GUARDIAN = 2 + 1 + 1 + 1 + 2 + 1 + 1 + 1 = 10

import random

# Declare points of each letter - Using dict
points = {'E':1, 'A':1, 'I':1, 'O':1, 'N':1, 'R':1, 'T':1, 'L':1, 'S':1, 'U': 1, 'D':2, 'G' : 2, 'B':3, 'C':3, 'M':3, 'P': 3,'F':4, 'H':4, 'V':4, 'W':4, 'Y': 4, 'K' : 5,'J':8, 'X': 8, 'Q':10, 'Z': 10 }

# Declare distribution of letters in bag
letter_distribution = {'K':1, 'J':1, 'X':1, 'Q':1, 'Z': 1,'B':2, 'C':2, 'M':2, 'P':2, 'F':2, 'H':2, 'V':2, 'W':2, 'Y': 2, 'G': 3, 'L':4, 'S':4, 'U':4, 'D': 4, 'N':6, 'R':6, 'T': 6, 'O' : 8, 'A':9, 'I' : 9, 'E': 12 }


bag_of_letters = []
# Function to generate bag
def create_bag(letters):
    for letter in letters:
        for i in range(letters[letter]):
            bag_of_letters.append(letter)
    
create_bag(letter_distribution)


# Function to randomize bag
def randomize_bag(bag):
    randomized_bag = random.shuffle(bag)
    return randomized_bag

randomize_bag(bag_of_letters)

print(bag_of_letters)


# Get tiles

# Find Valid word

# Get score