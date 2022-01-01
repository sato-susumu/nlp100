import pickle

import pandas as pd

model_path = './output/knock52.pkl'
with open(model_path, 'rb') as f:
    cv = pickle.load(f)
    le = pickle.load(f)
    lr = pickle.load(f)

for index, class_name in enumerate(le.classes_):
    print(f'カテゴリ {class_name}({index})')
    df = pd.DataFrame({
        'vocabulary': cv.vocabulary_.keys(),
        'coef': lr.coef_[index],
    })
    df_best = df.sort_values('coef', ascending=False)[:10]
    df_best.index = range(1, 11)
    print('best 10:\n', df_best)

    df_worst = df.sort_values('coef', ascending=True)[:10]
    df_worst.index = range(1, 11)
    print('worst 10:\n', df_worst)

    print('')
