# Q2 - Output to be int/float/string depending if the string can be converted to float or integer type

def convert(a=''):

    # Remove leading and trailing white spaces

    answer = a

    # Check if the string is a legal int value
    try:
        answer = int(a)
        return answer
    except:
        pass

    # Check if the string is a legal float value
    try:
        answer = float(a)
        return answer
    except:
        pass

    # Return as String type if both cases above don't work
    return a



