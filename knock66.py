import pandas as pd
from scipy.stats import spearmanr
from gensim.models.keyedvectors import KeyedVectors

# path = './data/googlenews-vectors-negative300.bin.gz'
word2vec_path = './data/googlenews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(word2vec_path, binary=True)


def calc_word2vec_score(x):
    return model.similarity(x['Word 1'], x['Word 2'])


path = './data/wordsim353/combined.csv'
df = pd.read_csv(path)
df['word2vec_score'] = df.apply(calc_word2vec_score, axis=1)
df['human_rank'] = df['Human (mean)'].rank(ascending=True, method='first')
df['word2vec_rank'] = df['word2vec_score'].rank(ascending=True, method='first')
print(df)

correlation, _ = spearmanr(df['human_rank'], df['word2vec_rank'] )
print(f'相関係数: {correlation}')

