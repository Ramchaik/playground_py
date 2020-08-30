def rec_sum(n):
    if n == 1 or n == 0:
        return n
    return n + rec_sum(n - 1)


print(rec_sum(10))
print(rec_sum(4))


def sum_func(n):
    if len(str(n)) == 1:
        return n

    return (n % 10) + sum_func(n // 10)


print(sum_func(4321))


def word_split2(phrase, list_of_words, output=None):
    if list_of_words == [] and phrase == "":
        return output

    if list_of_words == [] or phrase == "":
        return []

    word = list_of_words[0]

    if word in phrase:
        if output == None:
            output = []
        output.append(word)
        phrase = phrase.replace(word, "")

    return word_split(phrase, list_of_words[1:], output)


def word_split(phrase, list_of_words, output=None):
    if output is None:
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)

    return output


print(word_split('themanran', ['the', 'ran', 'man']))
print(word_split('ilovedogsJohn', [
      'i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
print(word_split('themanran', ['clown', 'ran', 'man']))
