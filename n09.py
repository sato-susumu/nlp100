import random


def get_typo(source: str) -> str:
    word_list = source.split(' ')
    result = []
    for word in word_list:
        if len(word) > 4:
            ch_list = [ch for ch in word]
            random_list = random.sample(ch_list[1:-1], len(ch_list[1:-1]))
            result.append(ch_list[0] + "".join(random_list) + ch_list[-1])
        else:
            result.append(word)
    return ' '.join(result)


text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human ' \
       'mind . '
print(get_typo(text))
