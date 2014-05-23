__author__ = 'Akkaash Goel'

from pycollections.node import BstNode
from pycollections.tree import BaseTree


class BstTree(BaseTree.BaseTree):
    def __init__(self, root_element=None):
        self.__root = BstNode.BstNode(root_element)
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

    def insert(self, element=None):
        new_node = BstNode.BstNode(element)
        if element is None:
            raise ValueError('Specified element is null')
        if self.is_empty():
            self.__root = new_node
        else:
            current = self.__root
            parent = None
            while current is not None:
                parent = current
                if current.get_element() == element:
                    raise ValueError('Element exists in Tree')
                elif element < current.get_element():
                    current = current.get_left()
                else:
                    current = current.get_right()

            if element < parent.get_element():
                parent.set_left(new_node)
                return new_node
            else:
                parent.set_right(new_node)
                return new_node

    def remove(self, element=None):
        if self.is_empty():
            raise ValueError('Tree is empty')
        if element is None:
            raise ValueError('Specified Node is null')
        current = self.__root
        parent = self.__root
        is_left_child = True
        while current is not None:
            parent = current
            if current.get_element() == element:
                if current == parent.get_left():
                    is_left_child = True
                else:
                    is_left_child = False
                break
            elif element < current.get_element():
                current = current.get_left()
            elif element > current.get_element():
                current = current.get_right()
        if current is None:
            raise ValueError('Element not found')