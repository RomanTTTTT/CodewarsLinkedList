'''This is a module docstring'''
class Node:
    '''Node class'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def get_nth(node, index):
    '''Gets nth node in a linked list'''
    if node is None:
        raise IndexError
    cur = node
    count = 0
    while count != index:
        cur = cur.next
        if cur is None:
            raise IndexError
        count += 1
    return cur
