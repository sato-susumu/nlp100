from gensim.models.keyedvectors import KeyedVectors

# path = './data/googlenews-vectors-negative300.bin.gz'
path = './data/googlenews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(path, binary=True)
result = model.similarity('United_States', 'U.S.')
print(f'similarity(United_States, U.S.) = {result}')
