# Q5 - Reformat this code to be more elegant - Operator selection

import operator
from Q2 import convert

def apply_operation(left_operand, right_operand, operator_input):

# Check if input arguments are of valid int or float type

    if type(convert(left_operand)) == str or type(convert(right_operand)) == str:  # convert function from Q2
        print "Input data not integer or float type"
        return

# Continue for valid input, using convert function from Q2 for appropriate conversion

    operator_table = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div}
    if operator_input not in operator_table:
        print "Invalid operator, try again"
        return
    else:

# Check for division by zero error

        try:
            return operator_table[operator_input](left_operand, right_operand)
        except:
            print "Division by zero is an invalid operation"
            return




