import re
from n20 import get_england_json


def get_england_lines() -> list:
    records = get_england_json()
    texts = [record['text'] for record in records]
    res = []
    for text in texts:
        for text_line in text.split('\n'):
            res.append(text_line)
    return res


if __name__ == '__main__':
    for line in get_england_lines():
        if re.search(r'\[\[Category:.*\]\]', line):
            print(line)
