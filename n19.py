import os
from collections import Counter

path = './data/popular-names.txt'
with open(path) as f:
    lines = f.readlines()
    name_list = [(line.split('\t')[0]) for line in lines]
    c = Counter(name_list)
    print(c.most_common())

os.system(f'cut -f 1 {path} | sort | uniq -c | sort -n -r')
