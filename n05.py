def get_word_bi_gram(word_list: list) -> list:
    return [
        [word_list[i], word_list[i + 1]] for i in range(len(word_list) - 1)
    ]


def get_ch_bi_gram(source: str) -> list:
    return [
        [source[i], source[i + 1]] for i in range(len(source) - 1)
    ]


text = 'I am an NLPer'
print(get_word_bi_gram(text.split(' ')))
print(get_ch_bi_gram(text))
