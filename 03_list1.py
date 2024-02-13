#!/usr/bin/python3 -tt

import sys

#importing the functions.py and using the methods specified in it
#from functions import printHeader
from functions1_simple import *

# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
def countFirstLastCharSame(words):
    count = 0
    if words is None or len(words) <= 0:
        return count
    for item in words:
        if len(item) >= 2 and item[0] == item[-1]:
            count += 1
    return count

# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
def sortOnXFirst(words):
    if words is None or len(words) <= 0:
        return words
    xlist = []
    list = []
    for item in words:
        if item.startswith("x"):
            xlist.append(item)
        else:
            list.append(item)
    newList = sorted(xlist) + sorted(list)
    return newList

# Extract the last element from a tuple -- used for custom sorting below.
def lastItemTupple(tuples):
    return tuples[-1]

# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
def sortTuplesOnLastItem(tuples):
    sortedTuple = sorted(tuples, key=lambda i: i[-1])
    return sortedTuple

def ListMethods():
    printHeader("builtInListMethods")
    printItemTab(f"{Fore.GREEN}append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort(), startswith(){Style.RESET_ALL}")
    print()

def main():
    ListMethods()
    
    printHeader("countFirstLastCharSame Test")
    list1 = ['aba', 'xyz', 'aa', 'x', 'bbb']
    list2 = ['', 'x', 'xy', 'xyx', 'xx']
    list3 = ['aaa', 'be', 'abc', 'hello']
    test(countFirstLastCharSame(list1), 3, list1)
    test(countFirstLastCharSame(list2), 2, list2)
    test(countFirstLastCharSame(list3), 1, list3)
    print()

    printHeader("sortOnXFirst Test")
    list4 = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
    list4TestOutcome = ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    list5 = ['ccc', 'bbb', 'aaa', 'xcc', 'xaa']
    list5TestOutcome = ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    list6 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    list6TestOutcome = ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    test(sortOnXFirst(list4), list4TestOutcome, list4)
    test(sortOnXFirst(list5), list5TestOutcome, list5)
    test(sortOnXFirst(list6), list6TestOutcome, list6)
    print()

    printHeader("sortTuplesOnLastItem Test")
    tuple1 = [(1, 3), (3, 2), (2, 1)]
    tuple1TestOutcome = [(2, 1), (3, 2), (1, 3)]
    tuple2 = [(2, 3), (1, 2), (3, 1)]
    tuple2TestOutcome = [(3, 1), (1, 2), (2, 3)]
    tuple3 = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
    tuple3TestOutcome = [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    test(sortTuplesOnLastItem(tuple1), tuple1TestOutcome, tuple1)
    test(sortTuplesOnLastItem(tuple2), tuple2TestOutcome, tuple2)
    test(sortTuplesOnLastItem(tuple3), tuple3TestOutcome, tuple3)
    print()

    

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
