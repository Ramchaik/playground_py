# Using Hashmap
def compress2(s):
    letters = {}
    final_str = ''

    for char in s:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    for char in letters:
        final_str += char + str(letters[char])

    return final_str


# Using Run Length Compression Algorithm
def compress(s):
    r = ""
    l = len(s)

    if l == 0:
        return ""

    if l == 1:
        return s+"1"

    cnt = 1
    i = 1

    while i < l:
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            r += (s[i - 1] + str(cnt))
            cnt = 1

        i += 1

    r += (s[i - 1] + str(cnt))

    return r


print(compress('AAAABBBcC'))
print(compress('AAB'))
