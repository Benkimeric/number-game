import random


def main():
    global randomNumber
    randomNumber = random.randrange(1, 101)
    # print(randomNumber)
    number = int(input("I have generated a Random number between 1 and 100, please guess it: "))
    guess(number)


# guess method with while loop to loop when user does not give correct guess
def guess(number1):
    correct = False
    while correct is False:
        if number1 > randomNumber:
            print("That is high. Try again with a lower number.")

        elif number1 < randomNumber:
            print("That is too low. Try again with a larger one.")

        elif number1 == randomNumber:
            print("Congratulations! You guessed it")
            break

        number1 = int(input("Guess again? Type your guess here: "))

# calling main method to run the guess method as well as generate first random number
main()
