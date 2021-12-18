from knock30 import load_neko_txt_mecab
import matplotlib.pyplot as plt
from collections import Counter
import japanize_matplotlib

lines = load_neko_txt_mecab()
word_counter = Counter()
for line in lines:
    for word in line:
        word_counter[word['surface']] += 1

best = word_counter.most_common(10)
print(best)

left = range(1, 11)
height = [word[1] for word in best]
labels = [word[0] for word in best]
plt.bar(left, height, tick_label=labels)
plt.xlabel('単語')
plt.ylabel('回数')
plt.title('出現頻度が高い10語')
plt.show()
