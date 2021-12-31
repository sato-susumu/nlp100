import pandas as pd
import nltk
import json


path_set_list = [
    ['train.txt', 'train.feature.txt'],
    ['valid.txt', 'valid.feature.txt'],
    ['test.txt', 'test.feature.txt'],
]
for path_set in path_set_list:
    df = pd.read_table(path_set[0])
    for index, value in df['title'].iteritems():
        words = nltk.word_tokenize(value)
        words = [Word.lower() for Word in words if Word.isalpha()]
        df.loc[index, 'feature'] = json.dumps(words)
    df.to_csv(path_set[1], sep='\t')
