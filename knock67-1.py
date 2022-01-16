import re
import pandas as pd
from gensim.models.keyedvectors import KeyedVectors
import pickle

input_path = './data/questions-words.txt'
output_path = './output/knock67.pickle'

category = ''
countries = []
with open(input_path, 'r') as fi:
    for line in fi.readlines():
        line = line[:-1]
        result = re.match(r'^: (.*)', line)
        if result:
            category = result.group(1)
            continue
        if category == 'capital-common-countries':
            words = line.split(' ')
            countries.append(words[1])

temp_df = pd.DataFrame(countries)
df = pd.DataFrame({'country': temp_df[0].unique()})
print(df)


# word2vec_path = './data/googlenews-vectors-negative300.bin.gz'
word2vec_path = './data/googlenews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(word2vec_path, binary=True)

df['vector'] = df['country'].apply(lambda x: model.get_vector(x))
print(df)
df.to_pickle(output_path)
