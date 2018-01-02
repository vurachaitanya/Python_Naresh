__author__ = 'Kalyan'

from placeholders import *

notes = '''
dicts are unordered sets of key value pairs which facilitate fast lookups by key.
'''

def test_dictionary_type():
    test_dict = {1 : "one"}   # note the new syntax
    assert __ == type(test_dict).__name__

def test_dictionary_empty():
    empty_dict_1 = {}
    assert __ == isinstance(empty_dict_1, dict)

    empty_dict_2 = dict() # another way of creating empty dict
    assert __ == len(empty_dict_2)

    assert empty_dict_1 == empty_dict_2

def test_dictionary_create():
    dict_1 = { 1 : "one", 2 : "two" }
    assert __ == isinstance(dict_1, dict)

    #init from a sequence of tuple pairs, useful in many cases.
    dict_2 = dict([(1, "one"), (2, "two")])
    assert __ == dict_2[1]
    assert __ == dict_2[2]

def test_dictionary_length():
    word_to_digit = { "one" : 1, "two" : 2}
    assert __ == len(word_to_digit) #note that a key value pair is treated as one item

def test_dictionary_is_indexed_by_key():
    word_to_digit = { "one" : 1, "two" : 2}
    assert __ == word_to_digit["one"]
    assert __ == word_to_digit["two"]

    try:
        word_to_digit[1]
    except Exception as ex:
    #Note that numeric indicies don't mean much like in case of lists and tuples
        print ex
        assert ___

def test_dictionary_is_mutable():
    word_to_digit = { "one" : 1, "two" : 2}

    word_to_digit["three"] = 3
    assert {__} == word_to_digit

    del word_to_digit["one"]
    assert {__} == word_to_digit

    word_to_digit["one"] = 10
    assert {__} == word_to_digit

def test_dictionary_is_unordered():
    dict1 = { 'one': 1, 'two': 2 }
    dict2 = { 'two': 2, 'one': 1}

    equal = (dict1 == dict2)
    assert __ == equal # True or False?

def test_dictionary_keys_and_values():
    word_to_digit = { "one" : 1, "two" : 2}
    assert __ == len(word_to_digit.keys())
    assert __ == len(word_to_digit.values())
    keys = word_to_digit.keys()
    #sort to get a deterministic order
    keys.sort()
    assert [__] == keys
    values = word_to_digit.values()
    values.sort()
    assert [__] == values

def test_dictionary_contains():
    word_to_digit = { "one" : 1, "two" : 2}

    assert __ == ("one" in word_to_digit)
    assert __ == ("two" in word_to_digit)

    assert __ == ("one" in word_to_digit.keys())
    assert __ == ("two" in word_to_digit.keys())

    assert __ == (1 in word_to_digit)
    assert __ == (2 in word_to_digit)

    assert __ == (1 in word_to_digit.values())
    assert __ == (2 in word_to_digit.values())

def test_valid_dictionary_keys():
    test_dict = {}
    test_dict[1] = 1
    test_dict["one"] = "string"
    try:
        key = []
        test_dict[key] = "list"
    except TypeError as te:
        print te  #observe the error message.
        assert ___

    try:
        key = (1,2)
        test_dict[key] = "tuple with immutable elements"
    except TypeError as te:
        print te
        assert ___ # do we reach here?

    try:
        key = (1, [])
        test_dict[key] = "tuple with mutable element"
    except TypeError as te:
        print te
        assert ___ #do we reach here?

    assert {__} == test_dict


# Apply what you have learnt in this lesson.
# Hint: See help(zip) in console or in online documentation
def make_dict(keys, values):
    """
    Returns a dictionary that maps keys to values correspondingly.
    Assume inputs are of same length.
    """
    return ___ # write a single line of code to create the dict.

import string

def test_make_dict():
    #map digits to their successors
    result = make_dict(range(10), range(1,11))
    for key, value in result.items():
        assert key + 1 == value

    # map numerical digits to their string values
    result = make_dict(range(10), string.digits)
    for key, value in result.items():
        assert value == str(key)
        assert key == int(value)


three_things_i_learnt = """
-
-
-
"""

notes2= '''
It is  good to understand how dictionaries are generally implemented under the hood.
Go through the the entire thread at
http://stackoverflow.com/questions/730620/how-does-a-hash-table-work
and discuss in the group if required.
'''