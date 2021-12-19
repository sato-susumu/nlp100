import re


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface  # 表層形
        self.base = base  # 基本形
        self.pos = pos  # 品詞
        self.pos1 = pos1  # 品詞細分類1

    def __str__(self):
        return f'{self.surface}'

    __repr__ = __str__


path = './data/ai.ja.txt.parsed'
results = []
with open(path, "r") as f:
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    tmp = []
    for line in lines:
        if re.match('^EOS', line):
            results.append(tmp)
            tmp = []
            continue
        if re.match('^\* ', line):
            continue
        (surface, others) = line.split('\t')
        other_list = others.split(',')
        tmp.append(Morph(surface, other_list[6], other_list[0], other_list[1]))

for morph in results[2]:
    print(f'{morph.surface} {morph.base} {morph.pos} {morph.pos1}')
