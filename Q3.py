# Q3 - Reformat this code to be more elegant - String Formatting

def reformat():

    abc = ['dog','Fido',10]

    #Removes the need for new variables to store intermediate values

    output = '{1} the {0} is {2} years old'.format(*abc)
    return output



#print reformat()
