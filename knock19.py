import os
import pandas as pd

path = './data/popular-names.txt'
df = pd.read_csv(path, sep='\t', header=None, names=['name', 'sex', 'count', 'year'])
for index, value in df['name'].value_counts().iteritems():
    print(index, ': ', value)

os.system(f'cut -f 1 {path} | sort | uniq -c | sort -n -r')
