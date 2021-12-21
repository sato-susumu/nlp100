import os
from collections import defaultdict

from knock41 import load_ai_ja_txt_parsed

if __name__ == '__main__':
    result = load_ai_ja_txt_parsed()

    out_path = 'knock45.txt'
    with open(out_path, 'w') as fw:
        for line in result:
            for chunk in line:
                if len(chunk.srcs) == 0:
                    continue
                if not chunk.has_verb():
                    continue
                base = chunk.get_verb(0).base
                particle_list = []
                for src in chunk.srcs:
                    if not line[src].has_particle():
                        continue
                    particle = line[src].get_particle(-1).surface

                    if particle not in particle_list:
                        particle_list.append(particle)

                fw.write(f'{base} {" ".join(particle_list)}\n')

    # コーパス中で頻出する「述語と格パターンの組み合わせ」
    os.system(f'sort {out_path} | uniq -c | sort -nr | head -n 10')
    print('')
    # 「行う」「なる」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
    os.system(f'grep -e 行う -e なる -e 与える {out_path} | sort | uniq -c | sort -nr | head -n 10')
