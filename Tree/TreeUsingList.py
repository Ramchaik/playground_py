def BinaryTree(r):
    return [r, [], []]


def insertLeft(r, val):
    t = r.pop(1)

    if len(t) > 1:
        r.insert(1, [val, t, []])
    else:
        r.insert(1, [val, [], []])

    return r


def insertRight(r, val):
    t = r.pop(2)

    if len(t) > 1:
        r.insert(2, [val, [], t])
    else:
        r.insert(2, [val, [], []])

    return r


r = BinaryTree(3)
print(insertLeft(r, 2))
print(insertLeft(r, 4))
print(insertLeft(r, 5))
print(insertRight(r, 5))
print(insertRight(r, 7))
print(insertRight(r, 9))
