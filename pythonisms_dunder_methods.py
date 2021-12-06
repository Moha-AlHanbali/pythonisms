"""This module is an examples demonstrating pythonic dunderr methods features"""


class Node():
    """
    Node class creates Node instances.
    If the node contains a falsy value it'll be considered as a falsy value itself.
    Arguments:
        value: any
        next_: Node
    """
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

    def __bool__(self):
        if not bool(self.value):
            return False
        else:
            return True