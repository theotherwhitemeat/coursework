#!/usr/bin/env python


class IndexOutOfRangeError(Exception):
    pass

class Node(object):
    """ Classic Node class for use in
    LinkedList. """

    def __init__(self, data=None):
        
        self._data = data
        self._next = None
        self._prev = None

    def setNext(self, item):
        """ Returns: None, sets next item. """
        self._next = item

    def getNext(self):
        """ Returns: item (type agnostic). """
        return self._next

    def setPrev(self, item):
        """ Returns: None, sets next item. """
        self._prev = item

    def getPrev(self):
        """ Returns: item (type agnostic). """
        return self._prev

    def getData(self):
        """ Returns: data (type agnostic). """
        return self._data

    def setData(self, data):
        """ Returns: None, sets data. """
        self._data = data


class LinkedList(object):
    """ LinkedList class. """

    def __init__(self):
        self._head = None

    def __str__(self):
        """ Returns: fancy string of items. """
        cur = self._head
        strout = ''
        while cur:
            strout += str(cur.getData())
            if cur.getNext():
                strout += ">>"
            else:
                break
            cur = cur.getNext()
        return strout

    def search(self, item):
        """ Returns: index (int) of item. """
        return self.index(item) is not None
    
    def index(self, item):
        """ Returns: index of item, or None. """
        n = 0
        cur = self._head
        while cur:
            # this comparison is sketchy because
            #  of duck-typing... but oh well!
            if cur.getData() == item:
                return n
            else:
                n += 1
                cur = cur.getNext()

    def add(self, item):
        """ Returns: None, places item at HEAD """
        newNode = Node(item)
        newNode.setNext(self._head)
        self._head = newNode

    def append(self, item):
        """ Returns: None, appends item to TAIL of list """
        cur = self._head
        while cur.getNext():
            cur = cur.getNext()
        cur.setNext(Node(item))

    def insert(self, index, item):
        """ Returns: None. Inserts item @ index. """
        cur = self._head
        prev = None
        next = cur.getNext()
        item = Node(item)
        n = 0
        while cur:
            if index == n:
                if n == 0:
                    self._head = item
                    item.setNext(cur)
                else:
                    prev.setNext(item)
                    item.setNext(cur)
                return
            elif n > index:
                raise IndexOutOfRangeError
            else:
                cur = cur.getNext()
                n += 1

    def pop(self, index=None):
        """ Returns: item (type agnostic). """
        cur = self._head
        prev = None
        n = 0
        while cur:
            if index and n == index:
                if n > 0:
                    prev.setNext(cur.getNext())
                else:
                    self._head = cur.getNext()
                return cur.getData()
            elif not cur.getNext() and not index:
                prev.setNext(None)
                return cur.getData()
            else:
                prev = cur
                cur = cur.getNext()
                n += 1
        if index > n:
            raise IndexOutOfRangeError

    def remove(self, item):
        """ Returns: None, removes item. """
        cur = self._head
        next = self._head.getNext()
        prev = None
        while cur is not None:
            if cur is self._head:
                #  cur  nex
                #  []>>>[]>>>[]
                self._head = next
                break
            elif prev:
                #  prev cur  nex
                #  []>>>[]>>>[]
                prev.setNext(next)
                break
            else:
                prev = cur
                cur = cur.getNext()
                if cur:
                    next = cur.getNext()

    def isEmpty(self):
        """ Returns: bool. """
        return self._head is None

    def size(self):
        """ Returns: size (int). """
        n = 0
        cur = self._head
        while cur:
            n += 1
            cur = cur.getNext()

        return n

    def getMiddle(self):
        """ Returns: middle Node element. """
        cur = self._head
        mid = self._head
        n = 0
        while cur:
            cur = cur.getNext()
            if (n % 2):
                mid = mid.getNext()
            n += 1
        return mid.getData()


if __name__ == '__main__':
    """ Validates Node, LinkedList. """

    nodeA, nodeB = Node(1), Node(2)
    nodeA.setNext(nodeB)
    nodeB.setPrev(nodeA)
    assert nodeA.getData() == 1
    assert nodeB.getData() == 2
    assert nodeA.getNext() is nodeB
    assert nodeB.getPrev() is nodeA

    tlist = LinkedList()
    tlist.add(1)
    print tlist
    assert tlist.search(1)
    assert tlist.index(1) == 0
    assert tlist.size() == 1
    tlist.add(2)
    print tlist
    assert tlist.index(1) == 1
    assert tlist.index(2) == 0
    assert tlist.search(1)
    assert tlist.size() == 2
    assert not tlist.isEmpty()

    tlist.append(3)
    tlist.append(4)
    print tlist
    assert tlist.__str__() == "2>>1>>3>>4"

    # test insert() and pop()
    tlist = LinkedList()
    tlist.add(2)
    tlist.insert(0, 1)
    tlist.insert(0, 0)
    assert tlist.index(0) == 0
    assert tlist.index(1) == 1
    assert tlist.index(2) == 2

    assert tlist.size() == 3
    assert tlist.pop() == 2
    assert tlist.size() == 2
    assert tlist.index(tlist.size() - 1) == tlist.pop(tlist.size() - 1)

    # test getMiddle()
    tlist = LinkedList()
    tlist.add(1)
    tlist.add(2)
    tlist.add(3)
    print tlist.getMiddle()
    assert tlist.getMiddle() == 2












