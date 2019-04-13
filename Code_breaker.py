###########################
### --- CODEBREAKER --- ###
###########################


# The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!


print("Welcome CODEBREAKER! You have to guess a three digit number.")
print("You will be given hints so you can make a better guess \n \n")


# random number generator and shuffler
def rand_gen():
    import random
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]


rand_num = rand_gen()

# Main function


def main():

    guess = input("What is your guess? ")

    if guess.isdigit() is True:
        list_guess = list(guess)
        # print(list_guess)

        if len(list_guess) == 3:

            if int(list_guess[0]) in rand_num and int(list_guess[1]) in rand_num and int(list_guess[2]) in rand_num and int(list_guess[0]) == rand_num[0] and int(list_guess[1]) == rand_num[1] and int(list_guess[2]) == rand_num[2]:
                print("Good Job! You guessed correctly")
                print("The number is: ", end='')
                print(rand_num[0], end='')
                print(rand_num[1], end='')
                print(rand_num[2], end='')

            elif int(list_guess[0]) in rand_num or int(list_guess[1]) in rand_num or int(list_guess[2]) in rand_num:

                if int(list_guess[0]) == rand_num[0] or int(list_guess[1]) == rand_num[1] or int(list_guess[2]) == rand_num[2]:
                    print("Match: You've guessed a correct number in the correct position \n")
                    main()

                elif int(list_guess[0]) != rand_num[0] and int(list_guess[1]) != rand_num[1] and int(list_guess[2]) != rand_num[2]:
                    print("Close: You've guessed a correct number but in the wrong position \n")
                    main()
            else:
                print("Nope: You haven't guess any of the numbers correctly \n")
                main()

        else:
            print("Only three digits are required! nothing more or less! \n")
            main()

    else:
        print("Please input a three digit number")
        main()

# print(rand_num)


main()
