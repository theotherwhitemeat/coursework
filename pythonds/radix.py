#!/usr/bin/env python
import sys
from random import random


def radix(items=None):
    if not items:
        items = [int(random() * 100) for x in xrange(0, int(random() * 100))]

    print "We haz items: %s" % items

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
    print items

if __name__ == '__main__':
    sys.exit(radix())
