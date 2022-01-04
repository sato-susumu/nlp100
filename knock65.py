import pandas as pd
from sklearn.metrics import accuracy_score

path = './output/knock64.csv'
df = pd.read_table(path, header=None, names=(
    'category', 'word1', 'word2', 'word3', 'word4', 'similar_word', 'score'))
semantic_analogy_df = df[~(df['category'].str.match('gram'))]
syntactic_analogy_df = df[df['category'].str.match('gram')]

print('Accuracy of semantic analogy = ',
      accuracy_score(semantic_analogy_df['word4'],
                     semantic_analogy_df['similar_word']))
print('Accuracy of syntactic analogy = ',
      accuracy_score(syntactic_analogy_df['word4'],
                     syntactic_analogy_df['similar_word']))
