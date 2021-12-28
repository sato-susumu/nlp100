import os
import pandas as pd

in_path1 = 'col1.txt'
in_path2 = 'col2.txt'
out_path1 = 'merge.txt'
df_name = pd.read_csv(in_path1, header=None, names=['name'])
df_sex = pd.read_csv(in_path2, header=None, names=['sex'])
df = pd.concat([df_name, df_sex], axis=1)
df.to_csv(out_path1, index=False, header=False, sep='\t')

os.system('paste col1.txt col2.txt > merge_cl.txt')
os.system('diff merge.txt merge_cl.txt')
