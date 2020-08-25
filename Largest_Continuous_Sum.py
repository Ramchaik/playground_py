def large_count_sum_with_interval(arr):
    size = len(arr)
    l_mx = g_mx = arr[0]
    st, f_idx = 0, 0

    for i in range(1, size):
        if l_mx + arr[i] > arr[i]:
            l_mx = l_mx + arr[i]
        else:
            l_mx = arr[i]
            st = i

        if g_mx < l_mx:
            g_mx = l_mx
            f_idx = i

    return [g_mx, st, f_idx]


def large_count_sum(arr):
    l_mx = g_mx = arr[0]

    for num in arr[1:]:
        l_mx = max(num, l_mx + num)
        g_mx = max(g_mx, l_mx)

    return g_mx


print(large_count_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))
print(large_count_sum_with_interval([1, 2, -1, 3, 4, 10, 10, -10, -1]))
