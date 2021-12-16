import os


path = './data/popular-names.txt'
with open(path) as f:
    for line in f.readlines():
        print(line.rstrip('\n').replace('\t', ' '))


os.system(f'cat {path} | sed -e "s/\\t/ /g"')
