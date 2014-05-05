#!/usr/bin/env python
from collections import defaultdict
import sys
import types  # types.FunctionType

# setup some examples, could be useful
exampleNums = [3, 6, 24, 6234, 2342, 2]
anagrams = ['hearst', 'earths']

def areAnagrams(words=None):
    """ Returns: bool.  True if words are
        anagrams, else false. """

    # Strategy:
    #  Populate dictionaries with chars and counts,
    #  then compare.

    if not words:
        words = anagrams

    worda, wordb = words
    wordaCounts, wordbCounts = defaultdict(int), defaultdict(int)

    # Early out: different lengths
    if len(worda) != len(wordb):
        return False

    for word, wordCount in zip((worda, wordb), (wordaCounts, wordbCounts)):
        for char in word:
            wordCount[char] += 1

    equal = (wordaCounts == wordbCounts)
    print "%s and %s are anagrams? %s" % (worda, wordb, equal)
    return equal


def minLinear(nums=None):
    """ Returns: smallest number from list in
        linear time. """

    # this is academic, as there's a min() function
    #  that runs in linear time already.  Oh well.

    if not nums:
        nums = exampleNums

    smallest = nums[0]

    for num in nums:
        if num < smallest:
            smallest = num

    print "Smallest: %d" % smallest
    return smallest            

def minSquared(nums=None):
    """ Returns: smallest number from list, but does
        by comparing each number with each number
        O(n**2). """

    # Let's have some default interaction
    if not nums:
        nums = exampleNums

    # O(n), so ignorable cheat
    smallest = max(nums)

    for i in nums:
        for j in nums:
            if i < j and i < smallest:
                smallest = i

    print "Smallest: %d" % smallest
    return smallest

def parChecker(symbolString):
    """ Returns: bool, assuring you of paren
        evenness, or your failure as a person. """

    from Stack import Stack

    # early out: uneven string
    if (len(symbolString) % 2):
        return False

    parens = Stack()
    for char in symbolString:
        if char == '(':
            parens.push(char)
        else:
            try:
                parens.pop()
            except:
                # unbalanced parens will puke
                return False

    return not(len(parens))

def evenChecker(symbolString):
    """ Returns: bool, of evenness of input string. """

    pairs = {')':'(', ']':'[', '}':'{'}
    openers, closers = pairs.values(), pairs.keys()

    from Stack import Stack

    # early out: uneven string
    if (len(symbolString) % 2):
        return False

    stack = Stack()

    for char in symbolString:
        if char in openers:
            stack.push(char)
        else:
            # bail if the stack empty, or if the chars don't match up
            if not len(stack) or (stack.peek() != pairs[char]):
                # early out
                return False
            else:
                stack.pop()

    return not(len(stack))

def divby2(num):
    """ Returns: binary version of number. """
    # this is an academic exercise, given the bin() function

    from Stack import Stack

    numstack = Stack()
    while num > 0:
        rem = num % 2
        if rem:
            numstack.push(1)
        else:
            numstack.push(0)
        num = num / 2

    binstring = ''
    while len(numstack):
        binstring += str(numstack.pop())
    return binstring

def getDupes(items=None):
    """ Returns: duplicate items. """

    from random import random
    if not items:
        items = [int(random()*100) for y in xrange(int(random()*20))]
    
    dupes = []
    itemSet = set()
    while items:
        item = items.pop()
        if item in itemSet:
            dupes.append(item)
        itemSet.add(item)

    print "Items: %s, dupes: %s" % (itemSet, dupes)

def reverseString(inputStr=None):
    """ Returns: reversed string. """

    from random import random

    numStr = ''.join([str(int(random()*100)) for x in xrange(int(random()*10))])
    revStr = numStr[::-1]
    print "Original str: %s, reversed str: %s" % (numStr, revStr)

if __name__ == '__main__':
    funcname = sys.argv[-1]
    if funcname in locals():
        func = locals()[funcname]
        func()
    else:
        funcs = [func for func in locals().values() if hasattr(func, '__call__')]
        print "What would you like me to run? %s " % funcs


