import pickle

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

input_path = './output/train.feature.txt'
output_path = './output/knock52.pkl'

df = pd.read_table(input_path)

cv = CountVectorizer()
X_train = cv.fit_transform(df['feature'])

le = LabelEncoder()
Y_train = le.fit_transform(df['category'])

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, Y_train)

with open(output_path, 'wb') as f:
    pickle.dump(cv, f)
    pickle.dump(le, f)
    pickle.dump(lr, f)
