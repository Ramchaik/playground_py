def my_balance_check(s):
    stack = []

    def update_stack(S, bracket):
        if S == []:
            S.append(bracket)
            return S

        else:
            top = len(S) - 1

            if bracket == ')' and S[top] == '(':
                S.pop()
                return S

            if bracket == ']' and S[top] == '[':
                S.pop()
                return S

            if bracket == '}' and S[top] == '{':
                S.pop()
                return S

            S.append(bracket)
            return S

    for bracket in s:
        stack = update_stack(stack, bracket)

    return len(stack) == 0


def balance_check(s):

    if len(s) % 2 != 0:
        return False

    opening = set('({[')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0


print(balance_check('()'))
print(balance_check('[][[()]]{{{}}}'))
print(balance_check('][[()]]{{{}}}'))
print(balance_check('()(){]}'))
