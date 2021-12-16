import re
from pprint import pprint

from n21 import get_england_lines

basic_dic = {}
for line in get_england_lines():
    obj = re.search(r'^\|(.*?)\s+=\s+(.*)', line)
    if obj:
        basic_dic[obj.group(1)] = obj.group(2)

pprint(basic_dic)
