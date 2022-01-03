from gensim.models.keyedvectors import KeyedVectors

# path = './data/googlenews-vectors-negative300.bin.gz'
path = './data/googlenews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(path, binary=True)
result = model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10)
print(f'most similar words = {result}')
