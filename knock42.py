from knock41 import load_ai_ja_txt_parsed

if __name__ == '__main__':
    result = load_ai_ja_txt_parsed()

    for line in result:
        for chunk in line:
            print(f'{chunk.surface}\t{line[chunk.dst].surface}')
