#!/usr/bin/python3 -tt

import sys

#importing the functions.py and using the methods specified in it
#from functions import printHeader
from functions1_simple import *


"""
Count donuts
when count is < 10 then return the donut count
When count > 10 then return it as many
"""
def countDonuts(count):
    if(count < 10):
        return 'Number of donuts: ' + str(count)
    else:
        return 'Number of donuts: many'
    
"""
Given a string s, return a string made of the first 2
and the last 2 chars of the original string,
so 'spring' yields 'spng'. However, if the string length
is less than 2, return instead the empty string.
"""
def bothEnds(s):
    if not s or len(s) < 2:
        return ''
    #first two characters
    firstTwo = s[0:2] #start at 0 index and pick two
    lastTwo = s[-2:] #pick the last two items, the reverse index starts from -1
    return f"{firstTwo}{lastTwo}"

"""
Given a string s, return a string
where all occurences of its first char have
been changed to '*', except do not change
the first char itself.
e.g. 'babble' yields 'ba**le'
Assume that the string is length 1 or more.
"""
def fixStartCharReplace(s):
    if not s or len(s) <= 1:
        return s
    first = s[0] #pick first char
    remaining = s[1:] #pick the rest of the string 
    replacedItem = remaining.replace(first, "*")
    return f"{first}{replacedItem}"

"""
Given strings a and b, return a single string with a and b separated
by a space '<a> <b>', except swap the first 2 chars of each string.
e.g.
  'mix', pod' -> 'pox mid'
  'dog', 'dinner' -> 'dig donner'
Assume a and b are length 2 or more.
"""
def mixUp(a, b):
    a_swapped = b[0:2] + a[2:]
    b_swapped = a[0:2] + b[2:]
    return a_swapped + ' ' + b_swapped

"""
test
"""
def test(got, expected, original):
    #putting colors, the import is in functions1_simple.py
    if(got == expected):
        prefix = f'{Fore.GREEN} OK {Style.RESET_ALL}'
    else:
        prefix = f'{Fore.RED} X {Style.RESET_ALL}'
    printItemTab(f'%s original: %s {Fore.BLUE}got: %s{Style.RESET_ALL} {Fore.CYAN}expected: %s{Style.RESET_ALL}' % (prefix, repr(original), repr(got), repr(expected)))
    

"""
Main
"""
def main():
    printHeader("countDonuts Test")
    test(countDonuts(4), 'Number of donuts: 4', 4)
    test(countDonuts(9), 'Number of donuts: 9', 9)
    test(countDonuts(10), 'Number of donuts: many', 10)
    test(countDonuts(99), 'Number of donuts: many', 99)
    print()

    printHeader("bothEnds Test")
    test(bothEnds('spring'), 'spng', 'spring')
    test(bothEnds('Hello'), 'Helo', 'Hello')
    test(bothEnds('a'), '', 'a')
    test(bothEnds('xyz'), 'xyyz', 'xyz')
    print()

    printHeader("fixStartCharReplace Test")
    test(fixStartCharReplace('babble'), 'ba**le', 'babble')
    test(fixStartCharReplace('aardvark'), 'a*rdv*rk', 'aardvark')
    test(fixStartCharReplace('google'), 'goo*le', 'google')
    test(fixStartCharReplace('donut'), 'donut', 'donut')
    print()

    printHeader("mixUp Test")
    test(mixUp('mix', 'pod'), 'pox mid', 'mix pod')
    test(mixUp('dog', 'dinner'), 'dig donner', 'dog dinner')
    test(mixUp('gnash', 'sport'), 'spash gnort', 'gnash sport')
    test(mixUp('pezzy', 'firm'), 'fizzy perm', 'pezzy firm')
    print()

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()