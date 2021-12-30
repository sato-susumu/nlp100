import os
import pandas as pd

path = './data/popular-names.txt'
df = pd.read_table(path, header=None, names=['name'], usecols=['name'])

for val in df['name'].sort_values().unique():
    print(val)

print('')
os.system(f' cut -f 1 {path} | sort | uniq')
