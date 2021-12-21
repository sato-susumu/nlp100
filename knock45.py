import os
from collections import defaultdict

from knock41 import load_ai_ja_txt_parsed

if __name__ == '__main__':
    result = load_ai_ja_txt_parsed()

    out_path = 'knock45.txt'
    with open(out_path, 'w') as fw:
        for line in result:
            dependency_dict = defaultdict(lambda: [])
            for chunk in line:
                if chunk.dst == -1:
                    continue
                dest_chunk = line[chunk.dst]
                if not chunk.has_particle():
                    continue
                if not dest_chunk.has_verb():
                    continue
                particle = chunk.get_particle(-1).surface
                base = dest_chunk.get_verb(0).base
                # print(f'{particle}\t{base}')
                if particle not in dependency_dict[base]:
                    dependency_dict[base].append(particle)

            for key, value_list in dependency_dict.items():
                fw.write(f'{key} {" ".join(value_list)}\n')

    # コーパス中で頻出する「述語と格パターンの組み合わせ」
    os.system(f'sort {out_path} | uniq -c | sort -nr | head -n 10')
    print('')
    # 「行う」「なる」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
    os.system(f'grep -e 行う -e なる -e 与える {out_path} | sort | uniq -c | sort -nr | head -n 10')
