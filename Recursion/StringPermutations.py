def permute2(s):
    output = []

    if len(s) == 1:
        return [s]

    for i, char in enumerate(s):
        perms = permute(s[:i] + s[i+1:])
        for perm in perms:
            output.append(char + perm)

    return output


def permute(s):
    out = []

    # Base Case
    if len(s) == 0:
        out = [s]

    else:
        # for every letter in string
        for i, char in enumerate(s):
            # for every permutations
            for perm in permute(s[:i] + s[i+1:]):
                # Add to output
                out += [char + perm]

    return out


print(permute('abc'))
