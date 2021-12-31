import pickle

model_path = './output/knock52.pkl'

with open(model_path, 'rb') as f:
    cv = pickle.load(f)
    le = pickle.load(f)
    lr = pickle.load(f)

title = 'Brian Williams To Set The Record About Those Rap Videos'
title_vec = cv.transform([title])
result = lr.predict(title_vec)[0]
proba = lr.predict_proba(title_vec)

print(f'予測された{result}')
print(le.inverse_transform([result])[0])
print(f'予測確率 {proba[0][result]}')
