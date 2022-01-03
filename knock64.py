import re
from gensim.models.keyedvectors import KeyedVectors

input_path = './data/questions-words.txt'
output_path = './output/knock64.csv'
# word2vec_path = './data/googlenews-vectors-negative300.bin.gz'
word2vec_path = './data/googlenews-vectors-negative300.bin'

model = KeyedVectors.load_word2vec_format(word2vec_path, binary=True)
category = ''

with open(input_path, 'r') as fi, \
        open(output_path, 'w') as fo:
    for line in fi.readlines():
        line = line[:-1]
        print(line)
        result = re.match(r'^: (.*)', line)
        if result:
            category = result.group(1)
            continue
        words = line.split(' ')
        result = model.most_similar(positive=[words[1], words[2]], negative=[words[0]])
        fo.write(f'{category}\t{words[0]}\t{words[1]}\t{words[2]}\t{words[3]}\t{result[0][0]}\t{result[0][1]}\n')
