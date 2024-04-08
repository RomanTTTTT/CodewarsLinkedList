'''This is a module docstring'''
class Node:
    '''Class of nodes'''
    def __init__(self, data):
        self.data = data
        self.next = None
def push(head, data):
    '''Push a node'''
    nod = Node(data)
    nod.next = head
    return nod
def build_one_two_three():
    '''Creates a 1 2 3 None linked list'''
    cur = push(None, 3)
    cur = push(cur, 2)
    cur = push(cur, 1)
