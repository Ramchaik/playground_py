import collections


def finder(arr1, arr2):
    look_up = {}

    for element in arr1:
        if element not in look_up:
            look_up[element] = 1
        else:
            look_up[element] += 1

    for element in arr2:
        if element in look_up:
            look_up[element] -= 1

    for element in look_up:

        if look_up[element] > 0:
            return str(element) + ' is the missing element.'

    return 'No missing element'


def finder2(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]


def finder3(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


def finder4(arr1, arr2):
    result = 0

    # Perform an XOR between the numbers in the arrays
    for num in arr1 + arr2:
        result ^= num

    return result


print('finder: ', finder([1, 2, 3], [2, 1]))
print('finder2: ', finder2([1, 2, 3], [2, 1]))
print('finder3: ', finder3([1, 2, 3], [2, 1]))
print('finder4: ', finder4([1, 2, 3], [2, 1]))
