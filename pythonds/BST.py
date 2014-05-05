#!/usr/bin/env python

class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None  # left leaf
        self.right = None  # right leaf
        self.level = None  # height?

class BST(object):

    def __init__(self):
        self.root = None

    def insert(self, val):
        """ Returns: None, inserts val. """
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, node, val):
        """ Returns: None, inserts node. """
        if val <= node.val:
            if node.left:
                self.insertNode(node.left, val)
            else:
                node.left = TreeNode(val)
        elif val > node.val:
            if node.right:
                self.insertNode(node.right, val)
            else:
                node.right = TreeNode(val)

    def find(self, val):
        """ Returns: TreeNode with val. """
        return self.findNode(self.root, val)

    def findNode(self, val):
        """ Returns: TreeNode with val. """
        if node is None:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self.findNode(node.left, val)
        else:
            return self.findNode(node.right, val)

    def preorder(self, root=None):
        """ Returns: None, executes preorder traversal. """
        if self.root:
            print self.root.val
            self.preorder()







if __name__ == '__main__':
    # Running directly?  Let's validate our BST!

