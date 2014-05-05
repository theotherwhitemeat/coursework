#!/usr/bin/env python

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        """ Returns: None.  Adds item to stack. """
        self.stack.append(item)

    def pop(self):
        """ Returns: item. Removes first item. """
        return self.stack.pop()

    def peek(self):
        """ Returns: first item """
        return self.stack[-1]

    def isEmpty(self):
        """ Returns: bool. """
        return not len(self.stack)

    def size(self):
        """ Returns: stack size. """
        return len(self.stack)

    def __len__(self):
        """ Returns: len, silly. """
        return self.size()

if __name__ == '__main__':
    """ Returns: nothing.  Validates Stack."""

    stacky = Stack()
    items = [1, 2, 3, 4, 5]
    map(stacky.push, items)

    for i, item in enumerate(items[::-1]):
        assert stacky.size() == (5 - i)
        assert not stacky.isEmpty()
        assert item == stacky.peek()
        assert item == stacky.pop()

    
