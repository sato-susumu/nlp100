from knock41 import load_ai_ja_txt_parsed
from graphviz import Digraph

if __name__ == '__main__':
    result = load_ai_ja_txt_parsed()
    tmp_dir_path = '/tmp'

    dg = Digraph(directory=tmp_dir_path, format='png')
    line_no = 2

    # ノード作成
    for i, chunk in enumerate(result[line_no]):
        if chunk.dst == -1 and len(chunk.srcs) == 0:
            continue
        dg.node(str(i), label=f"{i}:{chunk.surface}")

    # エッジ作成
    for i, chunk in enumerate(result[line_no]):
        if chunk.dst == -1:
            continue
        # dest_chunk = result[line_no][chunk.dst]
        # print(f'{chunk.surface}\t{dest_chunk.surface}')
        dg.edge(str(i), str(chunk.dst))

    dg.render(None, view=True)
