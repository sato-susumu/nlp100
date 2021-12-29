import pandas as pd
from sklearn.model_selection import train_test_split

path = "./data/NewsAggregatorDataset/newsCorpora.csv"
df = pd.read_table(path, names=[
    'id', 'title', 'url', 'publisher', 'category', 'story', 'hostname', 'timestamp'])
df = df.dropna().query('publisher == "Reuters" '
                       '| publisher == "Huffington Post" '
                       '| publisher == "Businessweek"'
                       '| publisher == "Contactmusic.com"'
                       '| publisher == "Daily Mail"')
print(df['publisher'].value_counts())

# デフォルトでシャッフルされるため、別途シャッフルしない
train_df, other_df = train_test_split(df, test_size=0.2)
test_df, valid_df = train_test_split(other_df, test_size=0.5)

columns = ['title', 'category']
train_df[columns].to_csv('train.txt', sep='\t', index=False, header=False)
test_df[columns].to_csv('test.txt', sep='\t', index=False, header=False)
valid_df[columns].to_csv('valid.txt', sep='\t', index=False, header=False)

print(f'df size = {len(df)}')
print(f'train size = {len(train_df)}')
print(f'test size = {len(test_df)}')
print(f'valid size = {len(valid_df)}')
print(f'train size + test size + valid size = {len(train_df) + len(test_df) + len(valid_df)}')
