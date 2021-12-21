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


if __name__ == '__main__':
    path = './data/ai.ja.txt.parsed'
    line_info_list = []
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]
        morphs = []
        for line in lines:
            if re.match(r'^EOS', line):
                line_info_list.append(morphs)
                morphs = []
                continue
            if re.match(r'^\* ', line):
                continue
            (surface, others) = line.split('\t')
            other_list = others.split(',')
            morphs.append(Morph(surface, other_list[6], other_list[0], other_list[1]))

    for morph in line_info_list[2]:
        print(f'{morph.surface} {morph.base} {morph.pos} {morph.pos1}')
