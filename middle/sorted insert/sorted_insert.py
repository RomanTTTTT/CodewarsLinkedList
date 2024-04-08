'''This is a module docstring'''
class Node:
    '''Class of nodes'''
    def __init__(self, data):
        self.data = data
        self.next = None
def sorted_insert(head, data):
    '''Inserts data into sorted linked list'''
    if head is None:
        return Node(data)
    cur = head
    while cur is not None:
        if cur.next is None:
            nod = Node(data)
            cur.next = nod
            break
        if cur.data >= data:
            nod = Node(data)
            nod.next = cur
            head = nod
            break
        if cur.data <= data <= cur.next.data:
            nod = Node(data)
            nod.next = cur.next
            cur.next = nod
            break
        cur = cur.next
    return head
