import pandas as pd
import nltk


path_set_list = [
    ['./output/train.txt', './output/train.feature.txt'],
    ['./output/valid.txt', './output/valid.feature.txt'],
    ['./output/test.txt', './output/test.feature.txt'],
]
for path_set in path_set_list:
    df = pd.read_table(path_set[0])
    for index, value in df['title'].iteritems():
        words = nltk.word_tokenize(value)
        words = [Word.lower() for Word in words if Word.isalpha()]
        df.loc[index, 'feature'] = ' '.join(words)
    df.to_csv(path_set[1], sep='\t')
