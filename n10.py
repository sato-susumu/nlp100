import os


path = './data/popular-names.txt'
with open(path) as f:
    print(len(f.readlines()))


os.system(f'wc -l {path}')
