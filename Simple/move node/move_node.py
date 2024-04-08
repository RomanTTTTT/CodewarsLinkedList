'''This is a module docstring'''
class Node:
    '''Node class'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class Context(object):
    '''Context class'''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
def move_node(source, dest):
    '''Moves a node'''
    des = source
    src = source.next
    des.next = dest
    return Context(src, des)
