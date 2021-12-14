import json


def get_country_json() -> list:
    path = './data/jawiki-country.json'
    with open(path, "r") as f:
        lines = f.readlines()
        decoder = json.JSONDecoder()
        tmp = [decoder.raw_decode(line) for line in lines]
        return [tmp_record[0] for tmp_record in tmp]


def get_england_json() -> list:
    country_json = get_country_json()
    res = []
    for data in country_json:
        if 'イギリス' == data['title']:
            res.append(data)
    return res


if __name__ == '__main__':
    for record in get_england_json():
        print(f'{record["text"]}\n')
