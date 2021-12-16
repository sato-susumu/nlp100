import re

from knock21 import get_england_lines

for line in get_england_lines():
    obj = re.search(r'\[\[Category:(.*)\]\]', line)
    if obj:
        print(obj.group(1))
