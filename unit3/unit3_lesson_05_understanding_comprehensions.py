__author__ = 'Kalyan'

notes = '''
 These features make creating lists, dicts and sets from other sequences easy and compact.
 lc -> list comprehensions
 dc -> dict comprehensions
 sc -> set comprehensions

 In python, these have largely replaced the usage of map and filter.
'''

from placeholders import *
import string

def is_even(x):
    return x%2 == 0

def square(x):
    return x*x

def test_lc_basic():
    input = [1,2,3]
    result = [2* x for x in input]
    assert __ == len(result)
    assert [__] == result

def test_lc_map_func():
    input = [1,2,3]
    result = [square(x) for x in input]
    assert [__] == result

def test_lc_trim_words():
    words = ["one\n", "two\n", " three\n"]
    result = [word.strip() for word in words]
    assert [__] == result

def test_lc_filter_func():
    input = range(10)
    result = [x for x in input if is_even(x)]
    assert [__] == result

def test_lc_filter_map():
    result = [square(x) for x in range(5) if is_even(x)]
    assert [__] == result

def test_lc_nested():
    result = [(x+y) for x in range(3) for y in range(3)]
    assert __ == len(result)
    assert [__] == result

def test_lc_nested_filter():
    result = [(x+y) for x in range(3) for y in range(3) if is_even(x+y)]
    assert __ == len(result)
    assert [__] == result

# dict comprehensions work the same way, you use them to create dicts
# from some source of data
def test_dc_basic():
    result = {i: chr(65+i) for i in range(4)} # note the braces
    assert __ == len(result)
    assert {__} == result

    result = {v: k for k,v in result.iteritems()}
    assert __ == len(result)
    assert {__} == result

def test_dc_mapping():
    result = { x : ord(x)-ord('A') + 1 for x in string.uppercase[:5] }
    assert __ == len(result)
    assert {__}== result

def test_dc_nested():
    result = { (x,y): x+y for x in range(2) for y in range(2)}
    assert __ == len(result)
    assert {__}== result

def test_dc_conditional():
    result = { x : x**2 for x in range (5) if x % 2 == 1}
    assert __ == len(result)
    assert {__} == result

# set comprehensions are very similar to dict comprehensions except that
# they deal a single value and create set objects
def test_sc_basic():
    result = { x*2 for x in range (4)}
    assert __ == len(result)
    assert {__}== result

def test_sc_nested():
    result = { x+y for x in range(3) for y in range(3)}
    assert __ == len(result)
    assert {__}== result

def test_sc_conditional():
    result = { x**2 for x in range (5) if x % 2 == 1}
    assert __ == len(result)
    assert {__} == result

def test_sc_filtering():
    all = set(range(10))
    evens = {x for x in all if x%2 == 0}
    assert __ == evens

    odds = {x for x in all if x%2 == 1}
    assert __ == odds

# apply what you have learnt to solve this problem. to create a dict that maps a letter to a scrabble score
# See: http://en.wikipedia.org/wiki/Scrabble_letter_distributions for more scrabble information.

# The tuples below give each score a letter has. For e.g score of E, A, O etc is 1
scrabble_scores = [(1, "EAOINRTLSU"), (2, "DG"), (3, "BCMP"),
                   (4, "FHVWY"), (5, "K"), (8, "JX"), (10, "QZ")]


# return a dict which contains a letter to score mapping.
# use dict comprehensions to create a dict from the above structure
def get_scrabble_scorer():
    pass

def test_scrabble_scorer():
    score_dict = get_scrabble_scorer()
    for score, letters in scrabble_scores:
        for letter in letters:
            assert score == score_dict.get(letter)


three_things_i_learnt = """
-
-
-
"""
