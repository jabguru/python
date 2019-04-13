def word_mix():

    def game_over():
        print("Game Over!")
        print("The correct word is: {}".format(gen_word))
        print("Your Total point is: {}\n".format(point))
        try_again = input("Do you want to try again? (Yes / No): ").lower()
        if try_again == "yes":
            word_mix()
        else:
            exit()

    # GAME PLAY
    print("\nWELCOME TO WORD-MIX 4.0!")
    print("A random word will be shuffled and given to you")
    print("You are to give the correct word and earn a point")
    print("You earn 10points for every 5 streaks!")
    print("You have access to hints from Level 3\n")

    # Importing Word list
    with open("words.txt") as word_file:
        english_words = list(word.strip().lower() for word in word_file)

        four_lw = []
        for x in english_words:
            if len(x) == 4:
                four_lw.append(x)

        five_lw = []
        for x in english_words:
            if len(x) == 5:
                five_lw.append(x)

        six_lw = []
        for x in english_words:
            if len(x) == 6:
                six_lw.append(x)

    # Importing random
    import random

    # Point and level start point
    point = 0
    level = 1

    def streak():

        if point in range(5, 100, 5):
            print("You are on a streak!")
            point += 10
            print("You have been given 10 points")
            print("You have {} point(s)".format(point))
        else:
            point = point

    # Game sequence
    while True:

        if level == 1:
            # Generate Word
            length = len(four_lw)
            f_length = length - 1
            number = random.randint(0, f_length)
            gen_word = four_lw[number]

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

                streak()

            else:
                game_over()

        elif level == 2:
            # Generate Word
            length = len(five_lw)
            f_length = length - 1
            number = random.randint(0, f_length)
            gen_word = five_lw[number]

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

                streak()

            else:
                game_over()

        elif level == 3:

            # Generate Word
            length = len(six_lw)
            f_length = length - 1
            number = random.randint(0, f_length)
            gen_word = six_lw[number]

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

            # Hint Generator
            print("\nDo You Need Hint? Hint Deducts 2points and reveals the first three letters.")
            hint_resp = (input("yes or no?: ").lower())
            if hint_resp == "yes":
                if point >= 2:
                    point -= 2
                    hint = list(gen_word)
                    hint = hint[:3]
                    print("Hint: ", end="")
                    print(hint[0], end="")
                    print(hint[1], end="")
                    print(hint[2], end="")
                    # User Input
                    answer = input("\nInput the correct word here: ")

                    if answer == gen_word:
                        point += 1
                        level += 1
                        print("Correct! You have {} point(s)".format(point))

                        streak()

                    else:
                        game_over()

                else:
                    print("Sorry You don't have upto 2points currently")
                    print("You have {} point".format(point))
                    # User Input
                    answer = input("\nInput the correct word here: ")

                    if answer == gen_word:
                        point += 1
                        level += 1
                        print("Correct! You have {} point(s)".format(point))

                        streak()

                    else:
                        game_over()
            else:
                # User Input
                answer = input("\nInput the correct word here: ")

                if answer == gen_word:
                    point += 1
                    level += 1
                    print("Correct! You have {} point(s)".format(point))

                    streak()

                else:
                    game_over()

        else:
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

            # Hint Generator
            print("\nDo You Need Hint? Hint Deducts 2points and reveals the first three letters.")
            hint_resp = (input("yes or no?: ").lower())
            if hint_resp == "yes":
                if point >= 2:
                    point -= 2
                    hint = list(gen_word)
                    hint = hint[:3]
                    print("Hint: ", end="")
                    print(hint[0], end="")
                    print(hint[1], end="")
                    print(hint[2], end="")
                    # User Input
                    answer = input("\nInput the correct word here: ")

                    if answer == gen_word:
                        point += 1
                        level += 1
                        print("Correct! You have {} point(s)".format(point))

                        streak()

                    else:
                        game_over()

                else:
                    print("Sorry You don't have upto 2points currently")
                    print("You have {} point".format(point))
                    # User Input
                    answer = input("\nInput the correct word here: ")

                    if answer == gen_word:
                        point += 1
                        level += 1
                        print("Correct! You have {} point(s)".format(point))

                        streak()

                    else:
                        game_over()
            else:
                # User Input
                answer = input("\nInput the correct word here: ")

                if answer == gen_word:
                    point += 1
                    level += 1
                    print("Correct! You have {} point(s)".format(point))

                    streak()


                else:
                    game_over()


word_mix()
