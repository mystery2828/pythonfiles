class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None

# def reverse(head):
#     current = head
#     prev = None
#     nextnode = None
#     while current:
#         nextnode = current.nextnode
#         current.nextnode = prev
#         prev = current
#         current = nextnode
#     return prev

def nth(m,head):
    left = head
    right = head
    for i in range(n-1):
        if not right.nextnode:
            raise LookupError('Error')
        right = right.nextnode
    while right.nextnode:
        left = left.nextnode
        right = right.nextnode
    return left
