from gensim.models.keyedvectors import KeyedVectors

# path = './data/googlenews-vectors-negative300.bin.gz'
path = './data/googlenews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(path, binary=True)
vector = model['United_States']
print(f'United_States vector: {vector}')
print(f'  length = {len(vector)}')
