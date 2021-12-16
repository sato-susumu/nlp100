def get_ch_bi_gram(source: str) -> list:
    return [
        source[i] + source[i + 1] for i in range(len(source) - 1)
    ]


text1 = 'paraparaparadise'
text2 = 'paragraph'
X = set(get_ch_bi_gram(text1))
Y = set(get_ch_bi_gram(text2))
print(X)
print(Y)
print(X | Y)
print(X - Y)
print(X & Y)
print('se' in X)
print('se' in Y)
