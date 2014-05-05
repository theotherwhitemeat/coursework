#!/usr/bin/env python

class Queue(object):

    def __init__(self):
        self.inq = []
        self.outq = []

    def __len__(self):
        """ Returns: int, size of queue. """
        return self.size()

    def enqueue(self, item):
        """ Returns: None.  Adds item to queue. """
        self.inq.append(item)

    def dequeue(self):
        """ Returns: item from queue. """
        if not len(self.outq):
            for item in self.inq[::-1]:
                self.outq.append(item)
            self.inq = []

        if not len(self.outq):
            return None
        else:
            return self.outq.pop()

    def size(self):
        """ Returns: int, size of queue. """
        return len(self.inq) + len(self.outq)

    def isEmpty(self):
        """ Returns: bool. """
        return not bool(self.size())


if __name__ == '__main__':
    """ Returns: None.  Validates queue. """

    queuey = Queue()
    items = [1, 2, 3, 4, 5]
    map(queuey.enqueue, items)

    for i, item in enumerate(items):
        assert queuey.size() == (5 - i)
        assert not queuey.isEmpty()
        qitem = queuey.dequeue()
        assert item == qitem

