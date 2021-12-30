import os
import pandas as pd
path = './data/popular-names.txt'
out_path1 = 'col1.txt'
out_path2 = 'col2.txt'
df = pd.read_table(path, header=None, names=['name', 'sex'], usecols=['name', 'sex'])
df['name'].to_csv(out_path1, index=False, header=False)
df['sex'].to_csv(out_path2, index=False, header=False)

os.system(f'cat {path} | cut -f1 > col1-cl.txt')
os.system(f'cat {path} | cut -f2 > col2-cl.txt')

os.system(f'diff col1.txt col1-cl.txt')
os.system(f'diff col2.txt col2-cl.txt')
