import re, random


def dice_roll(text):
    """
    Function returns a result of a dice roll with user defined number of dice and various dice types allowed. Result
    can be modified using a modifier. Packages required to be imported are 're' and 'random'.
    :param text: string denoting dice roll xDy+z, where:
                 x - number of dice
                 y - dice type, i.e. the number of dice sides. Valid dice types are: 3, 4, 6, 8, 10, 12, 20, 100
                 z - modifier added to or substracted from the result
    :return: result of a dice roll
    """
    try:
        # parsing the input string using regular expressions, labelling each number of dice, dice type and modifier
        regex = r'(?P<num>\d*)d(?P<type>3|4|6|8|10|12|20|100)(?P<modifier>(\+|-)?\d*)'
        r = re.search(regex, text, re.I)
        num = r.group('num')
        # handling null value number of dice. Default is 1 dice roll
        if num == "":
            num = 1
        # converting number of dice string into an integer
        else:
            num = int(num)
        # converting dice type string to integer
        type = int(r.group('type'))
        modifier = r.group('modifier')
        # handling null value modifier. Default is 0
        if modifier == "":
            modifier = 0
        # converting modifier string to integer
        else:
            modifier = int(modifier)
        # simulating a roll using a number of dice of a certain dice type, by generating a random integer from a range
        # of 1 to 'type' num-times and adding the results together
        result = 0
        for i in range(num):
            result += random.randint(1, type)
        # modifying the result by adding or substracting the modifier
        result += modifier
        # returning the modified dice roll result
        return result
    # handling errors from e.g. invalid dice type
    except AttributeError as e:
        print(f'Error: {e}. Try again.')

def main():
    print(dice_roll('17d3+12'))

if __name__=="__main__":
    main()