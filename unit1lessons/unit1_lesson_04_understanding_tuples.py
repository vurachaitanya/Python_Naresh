__author__ = 'Kalyan'

from placeholders import *

notes = '''
Tuples are yet another sequence type along the lines of strings and lists with
its own characteristics.
'''

def test_tuple_type():
    test_tuple = (1,2)   # note the syntax
    assert __ == type(test_tuple).__name__

def test_tuple_length():
    colors = ('red', 'blue', 'green')
    assert __ == len(colors)

def test_tuple_with_no_elements():
    empty = ()
    assert __ == isinstance(empty, tuple)
    assert __ == len(empty)

def test_tuple_with_one_element():
    test1 = (1)
    assert __ == type(test1).__name__

    test2 = (1,)  #note the syntax used to disambiguate
    assert __ == type(test2).__name__

def test_tuple_can_be_indexed():
    colors = ('red', 'blue', 'green')
    assert __ == colors[0]
    assert __ == colors[1]
    assert __ == colors[2]

def test_tuple_can_be_sliced():
    colors = ('red', 'blue', 'green')
    assert (__) == colors[1:3]
    assert (__) == colors[1:2]  #remember the awkward syntax for single element tuples :)


def test_tuples_are_immutable():
    colors = ('red', 'blue', 'green')
    try:
        colors[0] = 'orange'
    except TypeError as te:
        print te # note the exception
        assert ___

def test_tuples_can_be_nested():
    top_left = (10,20)
    bottom_right = (40,50)
    rectangle = (top_left, bottom_right)

    assert __ == len(rectangle)
    assert (__) == rectangle[0]
    assert __ == rectangle[0][0]
    assert __ == rectangle[1][1]


def test_tuple_unpacking():
    pair = (10, 20)
    a, b = pair
    assert __ == a
    assert __ == b

    triplet = (10, 20, 30)
    try:
        a, b = triplet
        assert False # should not come here.
    except ValueError as ve:
        print ve  # observe what is printed here.
        assert ___

def test_sequence_conversion():
    """
    sequences can be converted across forms using the builtin functions.
    """
    word = "testing"
    tup_1 = tuple(word)
    assert (__) == tup_1

    list_1 = list(word)
    assert [__] == list_1

    list_2 = list(tup_1)
    assert [__] == list_2

    word2 = str(tup_1)
    assert __ == word2

    word3 = "".join(tup_1)
    assert __ == word3

    word4 = "".join(list_1)
    assert __ == word4


def min_max(input):
    """
    Returns a tuple of min and max of the input list. Assume input is a non empty numeric list
    Use only builtin functions from: https://docs.python.org/2/library/functions.html
    """
    return ___  # write a line of code to return containing min and max

def test_min_max():
    a, b = min_max(range(1,10))
    assert a == 1
    assert b == 9

    a, b = min_max([12])
    assert a == 12
    assert b == 12


three_things_i_learnt = """
-
-
-
"""
