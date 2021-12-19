from knock30 import load_neko_txt_mecab
import matplotlib.pyplot as plt
from collections import Counter
import japanize_matplotlib

lines = load_neko_txt_mecab()


word_counter = Counter()
for line in lines:
    for word in line:
        word_counter[word['surface']] += 1

hist_data = [data[1] for data in word_counter.most_common()[::-1]]
print(hist_data)

plt.hist(hist_data, bins=20, range=(1, 20))
plt.show()
