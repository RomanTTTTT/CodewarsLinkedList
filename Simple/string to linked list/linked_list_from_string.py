'''This is a module docstring'''
class Node:
    '''Node class'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def linked_list_from_string(s):
    '''Creates a linked list from string'''
    lst = [int(i) for i in s.split(' -> ')[::-1][1:]]
    if not lst:
        return None
    list_of_el = [Node(lst[0], None)]
    for i in range(len(lst) - 1):
        list_of_el = [(Node(lst[i + 1], list_of_el[0]))] + list_of_el
    return list_of_el[0]
