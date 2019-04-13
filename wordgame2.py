# Word-Mix 2.0
# The aim is to generate random words and shuffle the so the user can arrange them and get the word correctly
# And as you get them you get points
# 10 points for every 5 level streak!
# then finally game over!

# GAME PLAY
print("\nWELCOME TO WORD-MIX 2.0!")
print("A random word will be shuffled and given to you")
print("You are to give the correct word and earn a point")
print("You earn 10points for every 5 streaks!\n")

# Importing Word list
with open("words.txt") as word_file:
    english_words = list(word.strip().lower() for word in word_file)

# Importing random
import random

# Point and level start point
point = 0
level = 1

# Game sequence
while True:
    # Generate Word
    number = random.randint(0, 370099)
    gen_word = english_words[number]

    # Shuffle word
    shuf_word = list(n for n in gen_word)
    random.shuffle(shuf_word)

    # Levels
    print("\nLEVEL {}: ".format(level))

    print(gen_word)

    # Print the scrambled word
    print("The word is: ", end="")
    for n in shuf_word:
        print(n, sep="", end="")

    # User Input
    answer = input("\nInput the correct word here: ")

    if answer == gen_word:
        point += 1
        level += 1
        print("Correct! You have {} point(s)".format(point))

        if point in range(5, 100, 5):
            print("You are on a streak!")
            point += 10
            print("You have been given 10 points")
            print("You have {} point(s)".format(point))
        else:
            continue

    else:
        print("Game Over!")
        print("The correct word is: {}".format(gen_word))
        print("Your Total point is: {}".format(point))
        break
