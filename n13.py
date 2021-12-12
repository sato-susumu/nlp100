import os

in_path1 = 'col1.txt'
in_path2 = 'col2.txt'
out_path1 = 'merge.txt'

with open(in_path1, 'r') as fr1, \
        open(in_path2, 'r') as fr2, \
        open(out_path1, 'w') as fw1:
    fr1_lines = fr1.readlines()
    fr2_lines = fr2.readlines()
    for fr1_line, fr2_line in zip(fr1_lines, fr2_lines):
        fw1.write(f'{fr1_line[:-1]}\t{fr2_line[:-1]}\n')


os.system('paste col1.txt col2.txt > merge_cl.txt')
os.system('diff merge.txt merge_cl.txt')
