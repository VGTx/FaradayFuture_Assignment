# Q1 - Class for implementing required functionality for a list of data

import collections

"""
    Implementation for a class that performs the following operations - 

    1. Initialise the list data field in the class using the constructor and store their current value throughout operations
    2. Append new data values to the end of the list
    3. Insert new data values at the user indicated index position in the list
    4. Return all unique items in the list
    5. Return all items from the list along with their corresponding frequencies

    The list accepts individual, list and dictionary type data values. Corresponding helper functions perform the necessary operations.
    
    This class uses the counter function from the collections library to find the frequency of the elements.
"""


class ListClass(object):
    items = None

    def __init__(self, input):

        # Initialise the list and counter

        self.items = input
        self.counter = collections.Counter(self.items)

    def AppendByType(self, data):

        # Check data type and select appropriate helper function

        if type(data) == str or type(data) == int or type(data) == float:
            self.SingleAppend(data)
        elif type(data) == list:
            self.ListAppend(data)
        elif type(data) == dict:
            self.DictionaryAppend(data)
        else:
            print "Unrecognized data type"

        print "{0} data successfully appended".format(type(data))

    def InsertByType(self, data, index):

        # Check data type and select appropriate helper function

        if type(data) == str or type(data) == int or type(data) == float:
            self.SingleInsertion(data, index)
        elif type(data) == list:
            self.ListInsert(data, index)
        elif type(data) == dict:
            self.DictionaryInsert(data, index)
        else:
            print "Unrecognized data type"
        print "{0} data successfully inserted at position {1}".format(type(data), index + 1)

    def GetUniqueList(self):

        # Return list consisting of unique values only

        unique_list = list()
        for key, value in self.counter.iteritems():
            unique_list.append(key)
        return unique_list

    def GetItemFrequency(self):

        # Return list consisting of elements of the list and their corresponding frequencies

        return self.counter

    def SingleInsertion(self, data, index):

        # Helper function for InsertByType for data of type str, int and float

        if data != None:
            if data in self.counter.keys():
                self.counter[data] += 1
            else:
                self.counter[data] = 1
            self.items.insert(index, data)

    def ListInsert(self, data, index):

        # Helper function for InsertByType for data of type list

        if data != None:
            for element in data:
                self.SingleInsertion(element, index)
                index += 1

    def DictionaryInsert(self, data, index):

        # Helper function for InsertByType for data of type dict

        if data.keys() != None:
            for key, value in data.iteritems():
                for itercount in range(value):
                    self.SingleInsertion(key, index)
                    index += 1

    def SingleAppend(self, data):

        # Helper function for AppendByType for data of type str, int and float

        if data != None:
            if data in self.counter.keys():
                self.counter[data] += 1
            else:
                self.counter[data] = 1
            self.items.append(data)

    def ListAppend(self, data):

        # Helper function for AppendByType for data of type list

        if data != None:
            for element in data:
                self.SingleAppend(element)

    def DictionaryAppend(self, data):

        # Helper function for AppendByType for data of type dict

        if data.keys() != None:
            for key, value in data.iteritems():
                for itercount in range(value):
                    self.SingleAppend(key)





