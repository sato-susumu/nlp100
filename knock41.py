import re

from knock40 import Morph


class Chunk:
    def __init__(self, dst):
        self.morphs = []
        self.srcs = []
        self.dst = dst


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
            current_chunk.morphs.append(morph)

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
