import os
from functools import cmp_to_key


def compare(a, b):
    a_2 = int(a.split('\t')[2])
    b_2 = int(b.split('\t')[2])
    return a_2 - b_2


path = './data/popular-names.txt'
with open(path) as f:
    lines = f.readlines()
    new_lines = sorted(lines, key=cmp_to_key(compare), reverse=True)
    for line in new_lines:
        print(line[:-1])


os.system(f'sort -r -n -k 3 {path}')
