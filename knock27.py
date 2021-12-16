import re
from pprint import pprint

from knock21 import get_england_lines

basic_dic = {}
for line in get_england_lines():
    obj = re.search(r'^\|(.*?)\s+=\s+(.*)', line)
    if obj:
        field_name = obj.group(1)
        value = re.sub(r'\'{2,5}', '', obj.group(2))
        value = re.sub(r'\[\[([^\]]*?)\|[^\]]*?]]', r'\1', value)
        value = re.sub(r'\[\[([^\]]*?)]]', r'\1', value)
        basic_dic[field_name] = value

pprint(basic_dic)
