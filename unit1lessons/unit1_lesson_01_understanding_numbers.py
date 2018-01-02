__author__ = 'Kalyan'

from placeholders import *

# For most of these tests use the interpreter to fill up the blanks.
# type(object) -> returns the object's type.

def test_numbers_types():
    assert "int" == type(7).__name__
    assert __ == type(7.5).__name__
    assert __ == type(10L).__name__

def test_numbers_int_arithmetic_operations():
    assert __ == 10 + 20
    assert __ == 10 * 20
    assert __ == 2 ** 5
    assert __ == 10 - 20
    assert __ == 7/3

def test_numbers_string_to_int():
    """hint: execute  print int.__doc__ in python console
       to find out what int(..) does"""
    assert __ == int("FF", 16)
    assert __ == int("77", 8)

def test_numbers_int_to_string():
    assert __ == oct(10)
    assert __ == hex(100)
    assert __ == bin(255)

def test_numbers_long():
    """Long is not the long in c"""
    assert __ == 2 ** 200

# Being comfortable with number bases mentally is important and it is routinely asked in interviews as quick test
# of a candidate.
#
# Replace the __ with the correct string representation by working it out on paper (don't use any code or console).
#
# Read the following links:
#           http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
#           https://docs.python.org/2/library/functions.html#int
def test_numbers_base():
    assert 255 == int(__, 2)
    assert 254 == int(__, 16)
    assert 121 == int(__, 7)
    assert 675 == int(__, 26)



three_things_i_learnt = """
-
-
-
"""
