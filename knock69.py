import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE


def plot_tsne(x, y, colormap=plt.cm.Paired):
    plt.figure(figsize=(8, 6))
    # clean the figure
    plt.clf()
    tsne = TSNE(n_components=2, random_state=0, perplexity=5)
    # tsne = TSNE(n_components=2, random_state=0, perplexity=5, metric="cosine")
    x_embedded = tsne.fit_transform(x)
    plt.scatter(x_embedded[:, 0], x_embedded[:, 1], c=y, cmap=colormap)
    plt.colorbar()
    plt.title("Embedding Space with t-SNE")
    plt.show()


input_path = './output/knock67.pickle'
df = pd.read_pickle(input_path)
kmeans_model = KMeans(n_clusters=5, random_state=10)
kmeans_model.fit(df['vector'].tolist())
labels = kmeans_model.labels_
plot_tsne(df['vector'].tolist(), labels)
