import random


def lotto():
    """
    Function imitating a lotto draw. The user inputs six numbers and the functions prints them in a sorted list,
    prints another list with six random numbers without repetitions and shows the result, i.e. the numebr of successful
    hits.
    :return: None
    """
    while True:
        # requesting user to input 6 numbers and turning the input into a list
        str_list = input("Please input your 6 lucky numbers (between 1 and 49) separated by spaces: ").split(" ")
        # checking if all inputs are numbers
        try:
            num_list = [int(x) for x in str_list]
        except ValueError:
            print("One of the numbers is not really a number. Check unnecessary spaces. Try again.")
            continue
        # checking for duplicates
        if len(num_list) != len(set(num_list)):
            print("Seems like you input a duplicate. Try again.")
        #checking is all numbers are in range 1-49
        elif any(i < 1 or i > 49 for i in num_list):
            print("At least one of the numbers is outside of range 1-49. Try again.")
        # checking is user input exactly 6 numbers
        elif len(num_list) != 6:
            print("Please input 6 numbers. Try again.")
        else:
            break
    # printing user numbers in sorted list
    print(f"Your numbers are: {sorted(num_list)}")
    # drawing 6 random numbers from range 1-49
    draw_result = random.sample(range(1, 50), 6)
    print(f"The draw results are: {draw_result}")
    # counting correct guesses
    correct_guesses = 0
    for i in num_list:
        if i in draw_result:
            correct_guesses += 1
    print(f"The number of correct guesses is: {correct_guesses}")

# initialize sample draw
def main():
    lotto()
if __name__=="__main__":
    main()