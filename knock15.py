import os
import pandas as pd


path = './data/popular-names.txt'
N = 5
df = pd.read_csv(path, header=None)
for _, val in df.tail(N).iterrows():
    print(val[0])

print('')
os.system(f'tail -n 5 {path}')
