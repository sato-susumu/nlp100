def cipher(source: str) -> str:
    result = ''
    for ch in source:
        if str.islower(ch):
            result += chr(219 - ord(ch))
        else:
            result += ch
    return result


text1 = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
text2 = cipher(text1)
text3 = cipher(text2)
print(text2)
print(text3)
print(text1 == text3)
