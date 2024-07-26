

def read_text():
    with open('text.txt', 'r') as file:
        return ''.join(file.readlines())


def count_words(text: str) -> dict[str, int]:
    words = text.lower().split()
    res = {}
    for word in words:
        count = res.get(word)
        if count is None:
            count = 0
        res[word] = count + 1
    return res


text = read_text()
res = count_words(text)
print(res)

