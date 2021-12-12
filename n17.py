import os


path = './data/popular-names.txt'
N = 5
with open(path) as f:
    lines = f.readlines()
    name_set = set([line.split('\t')[0] for line in lines])

print(name_set)
print('')
os.system(f' cut -f 1 {path} | sort | uniq')
