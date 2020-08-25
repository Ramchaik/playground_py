class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def reverse(node):
    prev = next = None
    cur = node

    while cur:
        next = cur.nextnode
        cur.nextnode = prev
        prev = cur
        cur = next

    return prev


def reverse2(head):
    current = head
    previous = None
    nextnode = None

    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode

    return previous


a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

print(a.nextnode.value)
print(b.nextnode.value)

reverse(a)
# reverse2(a)
print('###################')

print(c.nextnode.value)
print(b.nextnode.value)
