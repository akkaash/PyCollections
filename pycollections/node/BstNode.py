__author__ = 'Akkaash Goel'

from pycollections.node import BaseNode


class BstNode(BaseNode.BaseNode):
    def __init__(self, element=None, parent=None, left=None, right=None):
        self.__element = element
        self.__parent = parent
        self.__left = left
        self.__right = right

    def get_element(self):
        return self.__element

    def get_left(self):
        return self.__left

    def set_left(self, left):
        self.__left = left

    def set_right(self, right):
        self.__right = right

    def get_right(self):
        return self.__right

    def get_children(self):
        if self.__left is not None:
            yield self.__left
        if self.__right is not None:
            yield self.__right

    def get_parent(self):
        return self.__parent

    def __len__(self):
        return 1