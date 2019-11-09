import random


def guessing_game(low, high):
    """
    The function imitates a game where the user needs to guess the number randomly selected by the computer from
    a range defined by the user using the parameters. Package required to run: 'random'.

    :param low: the low limit of the possible number to be guessed by the user
    :param high: the high limit of the possible number to be guessed by the user
    :return: "Success!" string upon the user successfully guessing the number
    """
    # pick a random integer from a user defined range
    computers_choice = random.randint(low, high)
    while True:
        try:
            # prompt the user to guess the number
            players_choice = int(input("Guess the number: "))
            # prompt the user if the guess was too low or too high
            if computers_choice > players_choice:
                print("Too low!")
            elif computers_choice < players_choice:
                print("Too high!")
            else:
                return "Success!"
        # handle inputs which are not integers
        except ValueError:
            print("This is not a number. Try again.")

# initialize a sample game
def main():
    print(guessing_game(1, 100))

if __name__=="__main__":
    main()