import random


def guesser(number):
    count = 0
    while True:
        user_guess = input("Enter Quit for end the game.\nGuess a number between 1 and 100: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)

            if user_guess not in range(1, 100):
                print("Please enter a number between 1 and 100\n")

            elif user_guess in range(number-10, number+10):
                if user_guess == number:
                    print("You guessed correctly. You Win!!!\n")
                    print(f"You took {count+1} guesses.")
                    break
                print("Your user_guess is too close. Maybe greater than or less than the number!\n")

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
            print("Please enter a number this time!!!\n")
        count += 1


def main():

    print("Welcome to the game!\n")
    number = random.randint(1, 100)
    guesser(number)


if __name__ == "__main__":

    main()
