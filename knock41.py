import re

from knock40 import Morph


class Chunk:
    def __init__(self, dst):
        self.morphs = []
        self.srcs = []
        self.dst = dst
        self.surface = ''

    def append_morph(self, morph: Morph) -> None:
        self.morphs.append(morph)
        if morph.pos != '記号':
            self.surface += morph.surface

    def has_noun(self) -> bool:
        for morph in self.morphs:
            if morph.pos == '名詞':
                return True
        return False

    def has_particle(self) -> bool:
        for morph in self.morphs:
            if morph.pos == '助詞':
                return True
        return False

    def has_verb(self) -> bool:
        for morph in self.morphs:
            if morph.pos == '動詞':
                return True
        return False

    def get_verb(self, index: int) -> Morph:
        morph_list = []
        for morph in self.morphs:
            if morph.pos == '動詞':
                morph_list.append(morph)
        return morph_list[index]

    def get_particle(self, index: int) -> Morph:
        morph_list = []
        for morph in self.morphs:
            if morph.pos == '助詞':
                morph_list.append(morph)
        return morph_list[index]


def load_ai_ja_txt_parsed():
    path = './data/ai.ja.txt.parsed'
    line_info_list = []
    with open(path, "r") as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]
        current_chunk = None
        chunks = []
        for line in lines:
            if re.match(r'^EOS', line):
                line_info_list.append(chunks)
                chunks = []
                continue
            if re.match(r'^\* ', line):
                match = re.match(r'^\* \d+ ([-\d]+)D', line)
                current_chunk = Chunk(int(match.group(1)))
                chunks.append(current_chunk)
                continue
            (surface, others) = line.split('\t')
            other_list = others.split(',')
            morph = Morph(surface, other_list[6], other_list[0], other_list[1])
            current_chunk.append_morph(morph)

    for line in line_info_list:
        for i, chunk in enumerate(line):
            if chunk.dst == -1:
                continue
            line[chunk.dst].srcs.append(i)
    return line_info_list


if __name__ == '__main__':
    result = load_ai_ja_txt_parsed()

    for i, chunk in enumerate(result[2]):
        print(f'{i}: dst={chunk.dst} srcs={chunk.srcs}')
        for morph in chunk.morphs:
            print(f' {morph.surface} {morph.base} {morph.pos} {morph.pos1}')
