'''This is a module docstring'''
class Node(object):
    '''Class of nodes'''
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    '''Removes duplicates in a linked list'''
    cur = head
    visited = set()
    visited.add(head)
    while cur is not None:
        visited.add(cur.data)
        if cur.next is None:
            break
        if cur.next.data in visited:
            cur.next = cur.next.next
            continue
        cur = cur.next
    return head
