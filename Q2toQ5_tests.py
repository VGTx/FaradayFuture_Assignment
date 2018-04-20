from Q2 import convert as Q2_answer
from Q3 import reformat as Q3_answer
from Q4 import min_new as Q4_answer
from Q5 import apply_operation as Q5_answer

"""
Program to check test cases for Questions 2 to 5
"""

class Question2_testcases(object):

    def string_inputs(self):
        string_list = ["aa","012,34","(12)","NaN","Inf","two","None","2.03^10","False"," 5,45"]

        for element in string_list:
            assert isinstance(Q2_answer(element), str)

    def int_inputs(self):
        int_list = ["2","3","   4","5  ","-27"]

        for element in string_list:
            assert isinstance(Q2_answer(element), int)

    def float_inputs(self):
        float_list = ["2.0","3.0045","   4e5",".34","-23.67"]

        for element in string_list:
            assert isinstance(Q2_answer(element), float)

class Question3_testcases(object):

    def unformatted(self):

        abc = ['dog', 'Fido', 10]
        animal = abc[0]
        name = abc[1]
        age = abc[2]
        output = ('{name} the {animal} is {age} years old'.format(
            animal=animal, name=name, age=age))

        assert self.unformatted() == Q3_answer()

class Question4_testcases(object):

    def testcases(self):
        list = [0,2,3]
        assert Q4_answer(list[0],list[1],list[2]) == 0
        list = ['1','2',3]
        assert Q4_answer(list[0],list[1],list[2]) == 1
        list = ['a','b', 'c']
        assert Q4_answer(list[0], list[1], list[2]) == None
        list = ['1', '2', '3']
        assert Q4_answer(list[0],list[1],list[2]) == 1
        list = [1.0, 2.0, 3.0]
        assert Q4_answer(list[0],list[1],list[2]) == 1.0

class Question5_testcases(object):

    def testcases(self):
        list = [1, 2, '+']
        assert Q5_answer(list[0],list[1],list[2]) == 3
        list = [1, 2, '-']
        assert Q5_answer(list[0],list[1],list[2]) == -1
        list = ['1', '2', '+']
        assert Q5_answer(list[0],list[1],list[2]) == 3
        list = [1.0, 2.0, '*']
        assert Q5_answer(list[0],list[1],list[2]) == 2.0
        list = [4, 0, '/']
        assert Q5_answer(list[0],list[1],list[2]) == None




