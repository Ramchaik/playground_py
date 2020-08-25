def sentence_reversal(str):
    return ' '.join(reversed(str.split()))


def sentence_reversal2(str):
    return ' '.join(str.split()[::-1])


print(sentence_reversal('This is the best'))
print(sentence_reversal('  This is the   best  '))
print(sentence_reversal2('  This is the   best  '))
