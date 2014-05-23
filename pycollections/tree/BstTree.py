__author__ = 'Akkaash Goel'

from pycollections.node import BstNode
from pycollections.tree import BaseTree


class BstTree(BaseTree.BaseTree):
    def __init__(self, root=None):
        if root is not None and not isinstance(root, BstNode.BstNode):
            raise TypeError('Specified root should be of type BstNode')

        self.__root = root
        self.__size = 1

    def __len__(self):
        if self.__root is not None:
            return self.__size
        else:
            return 0

    def is_empty(self):
        return len(self) == 0

    def get_root(self):
        return self.__root

    def is_root(self, node):
        if not self.is_empty():
            if isinstance(node, BstNode.BstNode):
                return self.__root == node
            else:
                raise TypeError('Specified node should be of type BstNode')
        else:
            raise ValueError('Tree is empty')

    def insert(self, node=None):
        if node is None:
            raise ValueError('Specified node is null')
        if not isinstance(node, BstNode.BstNode):
            raise TypeError('Specified node should be of type BstNode')
        if self.is_empty():
            self.__root = node
        else:
            current = self.__root
            parent = None
            while current is not None:
                parent = current
                if current.get_element() == node.get_element():
                    raise ValueError('Element exists in Tree')
                elif node.get_element() < current.get_element():
                    current = current.get_left()
                else:
                    current = current.get_right()

            if node.get_element() < parent.get_element():
                parent.set_left(node)
            else:
                parent.set_right(node)