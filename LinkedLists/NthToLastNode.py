class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


def nth_to_last_node2(n, head):
    len_of_list = 0
    current = head
    while current:
        len_of_list += 1
        current = current.nextnode

    n_value = len_of_list - n
    if n_value < 0:
        return None

    idx = 0
    current = head
    while current:
        if idx == n_value:
            return current
        idx += 1
        current = current.nextnode


# Improved
def nth_to_last_node(n, head):
    left_ptr = right_ptr = head
    for _ in range(n-1):
        if not right_ptr.nextnode:
            raise LookupError("Error: n is larger than linked list")

        right_ptr = right_ptr.nextnode

    while right_ptr.nextnode:
        left_ptr = left_ptr.nextnode
        right_ptr = right_ptr.nextnode

    return left_ptr


target_node = nth_to_last_node(2, a)
print(target_node.value)
target_node = nth_to_last_node(4, a)
print(target_node.value)
