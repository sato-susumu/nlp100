import pandas as pd
from sklearn.cluster import AgglomerativeClustering

input_path = './output/knock67.pickle'

df = pd.read_pickle(input_path)

clustering_model = AgglomerativeClustering(n_clusters=5)
clustering_model.fit(df['vector'].tolist())
labels = clustering_model.labels_
print(labels)
df['label'] = labels
print(df[['country', 'label']].sort_values('label'))
