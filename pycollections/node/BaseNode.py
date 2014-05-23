__author__ = 'Akkaash Goel'


class BaseNode:
    def get_element(self):
        raise NotImplementedError('must be implemented by subclass')

    def get_children(self):
        raise NotImplementedError('must be implemented by subclass')

    def get_num_children(self):
        raise NotImplementedError('must be implemented by subclass')

    def get_parent(self):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self):
        if self.get_parent() is None:
            return True
        else:
            return False

    def is_leaf(self):
        if self.get_num_children() == 0:
            return True
        else:
            return False