import os


path = './data/popular-names.txt'
N = 5
with open(path) as f:
    lines = f.readlines()
    for line in lines[-N:]:
        print(line[:-1])

print('')
os.system(f'tail -n 5 {path}')
