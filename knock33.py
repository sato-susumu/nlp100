from knock30 import load_neko_txt_mecab

lines = load_neko_txt_mecab()
output = []
for line in lines:
    for i in range(1, len(line) - 1):
        if line[i - 1]['pos'] == '名詞' \
                and line[i]['surface'] == 'の' \
                and line[i + 1]['pos'] == '名詞':
            output.append(line[i - 1]['surface'] + line[i]['surface'] + line[i + 1]['surface'])

print(output)
