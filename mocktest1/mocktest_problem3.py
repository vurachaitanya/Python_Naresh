__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
This problem involves writing an iterator class that implements a CyclicCounter that take a value
and returns values from 0 to value and then down to 0 and then -value and back to 0 infinitely.

For e.g. for bound = 2. the iterator next() cycles through the values
0, 1, 2, 1, 0, -1, -2, -1, 0, 1, 2,  ...

Notes:
- implement the methods of the class so that it behaves like an iterator with behavior described above
- a negative value should raise ValueError
- no type checking required.
- you must use a constant amount of memory irrespective of the counter starting value (ie) I should be able to use
  really large values without running out of memory.
'''

class CyclicCounter(object):
    pass


# a basic test is given, write your own tests.
def test_counter():
    counter = CyclicCounter(2)

    # test the 1st 5 values
    result = []
    for index, value in enumerate(counter):
        if index == 5:
            break
        result.append(value)

    assert [0, 1, 2, 1, 0] == result
