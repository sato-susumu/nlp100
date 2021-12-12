import os

path = './data/popular-names.txt'
out_path1 = 'col1.txt'
out_path2 = 'col2.txt'
with open(path, 'r') as fr, \
        open(out_path1, 'w') as fw1, \
        open(out_path2, 'w') as fw2:
    for line in fr.readlines():
        data = line[:-1].split('\t')
        fw1.write(data[0] + '\n')
        fw2.write(data[1] + '\n')

os.system(f'cat {path} | cut -f1 > col1-cl.txt')
os.system(f'cat {path} | cut -f2 > col2-cl.txt')

os.system(f'diff col1.txt col1-cl.txt')
os.system(f'diff col2.txt col2-cl.txt')
