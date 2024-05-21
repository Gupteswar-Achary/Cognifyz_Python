import random


# Function to guess the number
def guesser(number, lower_range, upper_range):
    count = 0
    while True:
        user_guess = (input(f"Enter Quit for end the game.\nGuess a number between {lower_range} and {upper_range}: ").lower())

        # To check the user entered a number or not
        if user_guess.isdigit():
            user_guess = int(user_guess)

            # Check the guessed number is in between the range or not
            if user_guess not in range(lower_range, upper_range):
                print(f"Please enter a number between {lower_range} and {upper_range}\n")

            # Hints for the user
            elif user_guess in range(number - 10, number + 10):
                if user_guess == number:
                    print("\nYou guessed correctly. You Win!!!")
                    print(f"You took {count + 1} guesses. Now challenge your friends!")
                    break
                print("You are too close, maybe in the range of 10 greater than or less than the number.\n")

            elif user_guess < number:
                print("Your guess is too low\n")

            elif user_guess > number:
                print("Your guess is too high\n")

            else:
                pass

        elif user_guess == 'quit':
            while user_guess == 'quit':
                flag = input("Would you like to exit the game? (y/n): ").lower()
                if flag == 'y':
                    print(f"The number is {number}. Thanks for playing!")
                    quit()
                elif flag == 'n':
                    print("Keep Going!\n")
                    break
                else:
                    print("\nPlease enter y or n\n")

        else:
            print("\nPlease enter a number this time!!!\n")

        count += 1


# Function to select the difficulty level of the game
def select_difficulty():
    while 1:
        difficulty = input("Choose the difficulty: (High, Medium, Low): ").lower()
        if difficulty == "high":
            return difficulty
        elif difficulty == "medium":
            return difficulty
        elif difficulty == "low":
            return difficulty
        else:
            print("Wrong input")


def main():

    print("Welcome to the game!")

    # Function to select the difficulty
    # For high difficulty the range is in between (1 to 200)
    # For medium difficulty the range is in between (1 to 100)
    # For low difficulty the range is in between (1 to 50)
    level = select_difficulty()
    if level == "high":
        number = random.randint(1, 200)
        guesser(number, 1, 200)

    elif level == "medium":
        number = random.randint(1, 100)
        guesser(number, 1, 100)

    elif level == "low":
        number = random.randint(1, 50)
        guesser(number, 1, 50)

    else:
        print("Wrong input")


# Call the main function
if __name__ == "__main__":
    main()
