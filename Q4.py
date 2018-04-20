# Q4 - Minimum function that works for any number of input arguments
from Q2 import convert

def min_new(*args):

# Check if input arguments are of valid int or float type

    check = 0
    for input in args:
        if type(convert(input)) == str:     # convert function from Q2
            check += 1

    if check != 0:
        print "Input data not integer or float type"
        return None

# Continue for valid input, using convert function from Q2 for appropriate conversion

    min_current = convert(args[0])

    for input in args:
        if min_current > convert(input):
            min_current = convert(input)
    return min_current





