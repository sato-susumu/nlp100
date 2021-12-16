import re
import requests

from n21 import get_england_lines

basic_dic = {}
for line in get_england_lines():
    obj = re.search(r'^\|(.*?)\s+=\s+(.*)', line)
    if obj:
        field_name = obj.group(1)
        value = obj.group(2)
        basic_dic[field_name] = value

file_name = basic_dic['国旗画像']


S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": f"File:{file_name}",
    "iiprop": "url"
}
R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v["imageinfo"][0]["url"])
