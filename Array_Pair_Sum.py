def pair_sum2(arr, k):
    final_pairs = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                final_pairs.append([arr[i], arr[j]])

    print(final_pairs)
    return len(final_pairs)


def pair_sum(arr, k):
    look_up = {}
    n = len(arr)
    final_pairs = []

    for i in range(n):
        curr_num = arr[i]
        if curr_num in look_up:
            final_pairs.append([curr_num, look_up[curr_num]])
        else:
            look_up[abs(k - curr_num)] = curr_num

    print(final_pairs)
    return len(final_pairs)

# Using sets


def pair_sum_sets(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target, num), max(target, num)))

    print('\n'.join(map(str, list(output))))
    return len(output)


print(pair_sum_sets([1, 3, 2, 2], 4))
