import pandas as pd
from sklearn.cluster import KMeans

input_path = './output/knock67.pickle'

df = pd.read_pickle(input_path)

kmeans_model = KMeans(n_clusters=5, random_state=10)
kmeans_model.fit(df['vector'].tolist())
labels = kmeans_model.labels_
print(labels)
df['label'] = labels
print(df[['country', 'label']].sort_values('label'))
