'''This is a module docstring'''
class Node:
    '''Node class'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node):
    '''Stringifies a linked list'''
    if not node:
        return 'None'
    res = ''
    while node.next is not None:
        res += str(node.data) + ' -> '
        node = node.next
    res += str(node.data) + ' -> None'
    return res
