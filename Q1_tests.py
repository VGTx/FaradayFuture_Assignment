"""
Program to check test cases for Question 1
"""

from Q1 import ListClass


# Initialise list
a = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
b = ListClass(a)

# Print frequency of elements
print "Frequency of elements : "
print b.GetItemFrequency()

# Checking Append function
print "Checking Append functionality : "
b.AppendByType(23)
b.AppendByType('hello')
print b.items
print b.GetItemFrequency()
food = {"ham": 2, "egg": 3, 1: 3}
b.AppendByType(food)

# Print intermediate result
print "Intermediate result: "
print b.items

# Checking Insert function
print "Checking Insert functionality : "
b.SingleInsertion(0, 0)
print b.GetItemFrequency()
b.InsertByType(23, 0)
b.InsertByType('hello', 1)
print b.items
print b.GetItemFrequency()
food = {"ham": 2, "egg": 3, 1: 3}
b.InsertByType(food, 4)
listex = [99, 99, 99, 99, 99]
b.AppendByType(listex)
b.InsertByType(listex, 2)

# Print final result
print "Final result : "
print b.items

# Print Unique Element List
print "List of Unique Items: "
print b.GetUniqueList()