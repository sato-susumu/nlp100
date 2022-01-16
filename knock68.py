import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

input_path = './output/knock67.pickle'
df = pd.read_pickle(input_path)
Z = linkage(df['vector'].tolist(), method="ward", metric="euclidean")
fig = plt.figure()
dendrogram(Z, labels=df['country'].tolist(), orientation='right', color_threshold=4)
plt.show()
