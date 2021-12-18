from collections import Counter

from knock30 import load_neko_txt_mecab

lines = load_neko_txt_mecab()
word_counter = Counter()
for line in lines:
    for word in line:
        word_counter[word['surface']] += 1

print(word_counter.most_common())
