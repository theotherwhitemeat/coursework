#!/usr/bin/env python

class BubbleSorter(object):
    """ Bubble sort: iterate over sequence, comparing adjacent items
    and swapping them along the way.  O(n**2) """

    def __init__(self, seq):
        self._seq = seq
        self.sort()

    def __str__(self):
        """ Returns: str of sorted sequence. """
        return str(self._seq)

    def sort(self):
        """ Returns: None, sorts internal sequence. """

        seq = self._seq
        unsorted = True
        # We process list until no additional swaps are made
        #   ...that's how we know we're sorted.
        while unsorted:
            index = 0
            unsorted = False
            while index+1 < len(seq):
                # Swap items around if out of order
                if seq[index] > seq[index+1]:
                    seq[index], seq[index+1] = seq[index+1], seq[index]
                    unsorted = True
                index += 1
                #print "Iter: %s" % seq
            #print "unsorted: %s" % unsorted
        self._seq = seq
        #print seq

class SelectionSorter(object):
    """ Selection sort: find nth largest item, place at sequence[-n]. 
    O(n**2) """

    def __init__(self, seq):
        self._seq = seq
        self.sort()

    def sort(self):
        """ Returns: None, sorters internal sequence. """

        seq = self._seq
        unsorted = True
        iterations = 0
        while unsorted:
            # sentinel value
            unsorted = False
            iterations += 1
            largest = seq[0]
            n = 0
            for item in seq:
                if item > largest:
                    largest = item
                    unsorted = True
                n += 1
            # swap values, counting back from the end of the list
            seq[-iterations], seq[n] = seq[n], seq[-iterations]

class InsertionSorter(object):
    """ Insertion sort: start at item 0 in sequence, and build a sorted
    sublist by selecting an additional item, and swapping it into the
    correct place in the list, for example:

    : 5, 3, 8, 2
    : 3, 5, 8, 2
    : 2, 3, 5, 8
    """

    def __init__(self, seq):
        self._seq = seq
        self.sort()

    def sort(self):
        """ Returns: None, sorts internal sequence. """
        seq = self._seq
        for n in xrange(0, len(seq)-1):
            print seq
            while seq[n] > seq[n + 1]:
                seq[n], seq[n + 1] = seq[n + 1], seq[n]
                if n > 0:  # if we're past first position...
                    n -= 1  # go back one position
                else:
                    n += 1
        self._seq = seq
        print seq

class RadixSorter(object):
    """ Radix sort:
    1) Determine number of digits in largest number
    2) Iterate over numbers once for each number of digits, placing them in
        buckets according to the nth digit
    3) Dump buckets back into main list, and repeat for each digit

    [31, 1]
    [2, 42] --> 31, 1, 2, 42
    >>>>>>>
    [1, 2]
    [31]
    [42] --> 1, 2, 31, 42
    >>>>>>>
    """

    def __init__(self, seq):
        self._seq = self.sort(seq)

    def sort(items=None):
        if not items:
            items = [int(random() * 100) for x in xrange(0, int(random() * 100))]

        #print "We haz items: %s" % items

        # Determine maximum number of iterations necessary
        maxItem = max(items)
        maxLen = 1
        while maxItem:
            maxItem = maxItem / 10
            maxLen += 1

        # Create our buckets
        buckets = [list() for x in xrange(0, 10)]

        # Iterate once for each digit length
        for digitplace in xrange(1, maxLen):
            # Pop off each item from main list
            while items:
                item = items.pop()
                if item < (10 ** (digitplace - 1)):
                    # If divider is more than on digit
                    #  larger than item, place in bucket 0
                    bucknum = 0
                else:
                    # Determine value of item digit @ digitplace
                    bucknum = item / (10 ** (digitplace - 1)) % (10 ** digitplace)
                buckets[bucknum].append(item)
            for bucket in buckets:
                # Iterate over list backwards
                for item in bucket[::-1]:
                    items.append(item)
            buckets = [list() for x in xrange(0, 10)]
        return items

def getRandomSequence():
    """ Returns: random list of ints, 20 ints,
    int size: 0-100. """
    from random import random
    seq = [int(random() * 100) for x in xrange(0, 20)]
    return seq

if __name__ == '__main__':
    # If called directly, let's validate our sorter!

    randomSequence = getRandomSequence()
    sorter = InsertionSorter(randomSequence)


