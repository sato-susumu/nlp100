from knock30 import load_neko_txt_mecab

lines = load_neko_txt_mecab()
output = []
for line in lines:
    for word in line:
        if word['pos'] == '動詞':
            output.append(word['base'])

print(output)
