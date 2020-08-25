class DoublyLinkedListNode(object):
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None


a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next = b
b.prev = a

b.next = c
c.prev = b
