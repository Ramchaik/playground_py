def fib_rec2(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    return fib_rec2(n - 1) + fib_rec2(n - 2)


n = 10
cache = [None] * (n + 1)


def fib_dyp2(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    if cache[n-1]:
        return cache[n-1]
    else:
        cache[n-1] = fib_dyp2(n - 1) + fib_dyp2(n - 2)
        return cache[n-1]


def fib_itr2(n):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    a = b = 1
    c = 0
    for _ in range(n - 2):
        c = a + b
        a = b
        b = c

    return c


################################################################


def fib_itr(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a+b

    return a


def fib_rec(n):
    if n == 0 or n == 1:
        return n

    return fib_rec(n - 1) + fib_rec(n - 2)


n = 10
cache = [None] * (n + 1)


def fib_dyp(n):
    if n == 0 or n == 1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fib_dyp(n - 1) + fib_dyp(n - 2)
    return cache[n]


print(fib_rec(10))
print(fib_dyp(10))
print(fib_itr(10))
