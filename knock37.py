from knock30 import load_neko_txt_mecab
import matplotlib.pyplot as plt
from collections import Counter
import japanize_matplotlib

lines = load_neko_txt_mecab()


def has_neko(line: list) -> bool:
    for word in line:
        if word['surface'] == '猫':
            return True
    return False


word_counter = Counter()
for line in lines:
    if has_neko(line):
        print([word['surface'] for word in line])
        for word in line:
            if word['surface'] == '猫':
                continue
            word_counter[word['surface']] += 1

best = word_counter.most_common(10)
print(best)

left = range(1, 11)
height = [word[1] for word in best]
labels = [word[0] for word in best]
plt.bar(left, height, tick_label=labels)
plt.xlabel('単語')
plt.ylabel('回数')
plt.title('「猫」と共起頻度の高い上位10語')
plt.show()
