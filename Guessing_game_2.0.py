def guessing_game(min, max):
    """
    The function is a reverse guessing game where the user thinks a number in a range specified in the function
    parameters. The computer takes attempts to guess it and is prompted by the user of whether the guess is too high,
    too low or successful
    :param min: low limit of the guessing range
    :param max: high limit of the guessing range
    """
    print(f"Think of a number between {min} and {max} and I will try to guess it")
    success = False
    # loop to play until the computer guesses the number
    while success == False:
        # defining first guess
        guess = round(((max - min)/2) + min)
        print(f"My guess is: {guess}")
        # getting input from the user
        result = input("How did I do (too low/too high/success): ").lower()
        # divide and conquer to arrive at the right guess
        if result == "too high":
            max = guess
        elif result == "too low":
            min = guess
        elif result == "success":
            print("I won!")
            success = True
        else:
            print("Don't cheat!")

# initialize a sample game
def main():
    guessing_game(0, 100)

if __name__=="__main__":
    main()