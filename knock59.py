import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC


def load_x_y(path: str, le: LabelEncoder, cv: CountVectorizer, fit_and_transform: bool):
    df = pd.read_table(path)
    if fit_and_transform is True:
        x = cv.fit_transform(df['feature'])
        y = le.fit_transform(df['category'])
    else:
        x = cv.transform(df['feature'])
        y = le.transform(df['category'])
    return x, y


def calculate_accuracy(model, x, y):
    pred = model.predict(x)
    return accuracy_score(y, pred)


def main():
    cv = CountVectorizer()
    le = LabelEncoder()
    x_train, y_train = load_x_y('./output/train.feature.txt', le, cv, True)
    x_test, y_test = load_x_y('./output/test.feature.txt', le, cv, False)
    x_valid, y_valid = load_x_y('./output/valid.feature.txt', le, cv, False)

    c_list = [0.001, 0.01, 0.1, 1, 10, 100]
    df = pd.DataFrame()
    for c in c_list:
        print(f'C={c}')
        # model = LogisticRegression(max_iter=1000, C=c)
        model = SVC(kernel='linear', random_state=None, C=c)

        model.fit(x_train, y_train)
        df = df.append({
            'train': calculate_accuracy(model, x_train, y_train),
            'test': calculate_accuracy(model, x_test, y_test),
            'valid': calculate_accuracy(model, x_valid, y_valid),
        }, ignore_index=True)
    df.index = [str(c) for c in c_list]
    print(df)
    df.plot(kind='line')
    plt.show()


main()
