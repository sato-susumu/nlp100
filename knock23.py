import re

from knock21 import get_england_lines

for line in get_england_lines():
    obj = re.search(r'(={2,})\s*([^=]*)\s*(={2,})', line)
    if obj:
        level = len(obj.group(1)) - 1
        name = obj.group(2)
        print(f'{level} {name}')
