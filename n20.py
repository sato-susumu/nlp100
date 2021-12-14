import json

path = './data/jawiki-country.json'

with open(path, "r") as f:
    lines = f.readlines()
    res = []
    decoder = json.JSONDecoder()
    tmp = [decoder.raw_decode(line) for line in lines]
    json_data = [data[0] for data in tmp]

for data in json_data:
    if 'イギリス' in data['title']:
        print(data['text'])
        print()
