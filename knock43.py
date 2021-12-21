from knock41 import load_ai_ja_txt_parsed

if __name__ == '__main__':
    result = load_ai_ja_txt_parsed()

    for line in result:
        for chunk in line:
            if chunk.dst == -1:
                continue
            dest_chunk = line[chunk.dst]
            if not chunk.has_noun():
                continue
            if not dest_chunk.has_verb():
                continue
            print(f'{chunk.surface}\t{dest_chunk.surface}')
