__author__ = 'Akkaash Goel'


class BaseTree:
    def __init__(self):
        pass

    def get_root(self):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_empty(self):
        return len(self) == 0

