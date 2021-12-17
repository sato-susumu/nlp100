from knock30 import load_neko_txt_mecab

lines = load_neko_txt_mecab()
output = []
for line in lines:
    noun_block = ''
    for word in line:
        if word['pos'] == '名詞':
            noun_block += word['surface']
        else:
            if len(noun_block) > 0:
                output.append(noun_block)
                noun_block = ''
    if len(noun_block) > 0:
        output.append(noun_block)

print(output)
