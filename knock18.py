import os
import pandas as pd

path = './data/popular-names.txt'
df = pd.read_table(path, header=None, names=['name', 'sex', 'count', 'year'])
df.sort_values(by='count', ascending=False, inplace=True)
for _, values in df.head(5).iterrows():
    print(f'{values[0]}\t{values[1]}\t{values[2]}\t{values[3]}')

print('')
# 「2>/dev/null」でエラー出力を無視する
os.system(f'sort -r -n -k 3 {path} 2>/dev/null | head -n 5')
