def factorial(n):
    # Base case
    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(3))
print(factorial(4))
print(factorial(5))
