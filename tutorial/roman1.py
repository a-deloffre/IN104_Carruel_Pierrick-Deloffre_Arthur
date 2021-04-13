"""Convert to and from Roman numerals
This program is part of "Dive Into Python", a free Python book for
experienced programmers.  Visit http://diveintopython.org/ for the
latest version.
"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.2 $"
__date__ = "$Date: 2004/05/05 21:57:20 $"
__copyright__ = "Copyright (c) 2001 Mark Pilgrim"
__license__ = "Python"

#Define exceptions
class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))

def toRoman(n):

	if n > 3999:
		raise OutOfRangeError('number out of range (must be less than 4000)')

	if n <= 0:
		raise OutOfRangeError('number out of range (must be positive)')

	result = ''
	for numeral, integer in roman_numeral_map:
		while n >= integer:
			result += numeral
			n -= integer
	return result

def fromRoman(s):
    """convert Roman numeral to integer"""
    pass

