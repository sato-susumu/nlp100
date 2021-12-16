from pprint import pprint


def load_neko_txt_mecab() -> list:
    path = './data/neko.txt.mecab'
    result = []
    with open(path, "r") as f:
        lines = f.readlines()
        tmp = []
        for line in lines:
            if line == 'EOS\n':
                result.append(tmp)
                tmp = []
                continue
            if '\t' not in line:
                continue
            (surface, other) = line.split('\t')
            other_list = other.split(',')
            tmp.append({
                'surface': surface,  # 表層形
                'base': other_list[6],  # 基本形
                'pos': other_list[0],  # 品詞
                'pos1': other_list[1],  # 品詞細分類1
            })
        return result


if __name__ == '__main__':
    lines = load_neko_txt_mecab()
    pprint(lines)
