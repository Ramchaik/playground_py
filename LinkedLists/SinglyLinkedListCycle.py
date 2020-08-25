class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def check_cycle(node):
    slow = fast = node

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def check_cycle2(node):
    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next != None:
        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker1 == marker2:
            return True

    return False


##########
# List 1
##########
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
# c.next = a
##########

##########
# List 2
##########
A = Node(1)
B = Node(2)
C = Node(3)
##########

A.next = B
B.next = C
C.next = A
###########
print('has a loop ?', check_cycle(a))
print('has a loop ?', check_cycle(A))
