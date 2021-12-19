from knock30 import load_neko_txt_mecab
import matplotlib.pyplot as plt
from collections import Counter
import japanize_matplotlib

lines = load_neko_txt_mecab()


word_counter = Counter()
for line in lines:
    for word in line:
        word_counter[word['surface']] += 1

x = []
y = []
for i, data in enumerate(word_counter.most_common()):
    x.append(i + 1)
    y.append(data[1])

plt.plot(x, y)
ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
plt.show()
