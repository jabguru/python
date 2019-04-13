# Word Game 1.0
# The aim is to generate random words and shuffle the so the user can arrange them and get the word correctly


def rand_word():

    # Importing Word list
    with open("words.txt") as word_file:
        english_words = list(word.strip().lower() for word in word_file)

    # Random Word Generator
    import random

    # Generate Word
    number = random.randint(0, 370099)
    gen_word = english_words[number]
    print(gen_word)

    # Shuffle word
    shuf_word = list(n for n in gen_word)
    random.shuffle(shuf_word)

    # GAME PLAY
    print("WELCOME WORLD-MIX 1.0!")
    print("A random word will be shuffled and given to you")
    print("You are to give the correct word\n\n")
    print("The word is: ", end="")

    for n in shuf_word:
        print(n, sep="", end="")

    # Game sequence
    while True:
        # User Input
        answer = input("\n Input the correct word here: ")

        if answer == gen_word:
            print("Correct! You Got it.")
            break

        else:
            print("Wrong! Please try again!")
            print("The word is: {}".format(gen_word))


rand_word()
