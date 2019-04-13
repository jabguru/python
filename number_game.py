# Number Game 1.0

# Generate a random number
import random

number = random.randint(0, 20)
print(number)

while True:
    # request input from the user
    guess = input("Guess the number: ")

    # If the user doesnt enter an integer, tell him to
    if guess.isdigit() is True:

        # Convert the input string to integer
        guess = int(guess)

        # Checking the guess
        if guess == number:
            print("Your head is there! you got it")
            break
        else:
            print("Oga ade try again! You didnt get it")
    else:
        print("Please input a number\n")
