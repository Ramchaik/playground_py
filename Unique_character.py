def uniq_char2(s):
    letters = sorted(s)
    size = len(letters)

    for i in range(1, size):
        if letters[i] == letters[i - 1]:
            return False

    return True


def uniq_char3(s):
    return len(set(s)) == len(s)


def uniq_char(s):
    chars = set()

    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True


print(uniq_char('abd'))
