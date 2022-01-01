import pickle
import pandas as pd
from sklearn.metrics import accuracy_score


def calculate_score(name: str, path: str):
    df = pd.read_table(path)
    y_true = le.transform(df['category'])
    y_pred = lr.predict(cv.transform(df['feature']))
    print(f'{name} accuracy = {accuracy_score(y_true=y_true, y_pred=y_pred)}')


model_path = './output/knock52.pkl'
with open(model_path, 'rb') as f:
    cv = pickle.load(f)
    le = pickle.load(f)
    lr = pickle.load(f)

calculate_score('train', './output/train.feature.txt')
calculate_score('test', './output/test.feature.txt')

