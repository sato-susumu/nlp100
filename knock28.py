import re
from pprint import pprint

from knock21 import get_england_lines

basic_dic = {}
for line in get_england_lines():
    obj = re.search(r'^\|(.*?)\s+=\s+(.*)', line)
    if obj:
        field_name = obj.group(1)
        value = obj.group(2)
        # 強調除去
        value = re.sub(r'\'{2,5}', '', value)
        # タグ除去
        value = re.sub(r'<\w.*?/>', r'', value)
        value = re.sub(r'<\w.*?>', r'', value)
        value = re.sub(r'</\w.*?>', r'', value)
        # TODO: どれを残すか不明なので、最後を残す。他の回答を見て見直し
        # 説明ありテンプレート → 説明のみ残す
        value = re.sub(r'\{\{[^\}]*\|([^\}]+?)\}\}', r'\1', value)
        # 説明なしテンプレートのみ → 削除
        value = re.sub(r'\{\{[^}]+}}', r'', value)
        # 説明なしハイパーリンク → 削除
        value = re.sub(r'\[http[^]]+]', r'', value)
        # 説明文ありファイル → 説明のみ残す
        value = re.sub(r'\[\[[^\}]*\|([^\}]+?)\]\]', r'\1', value)
        # 説明文なしファイル → パスのみ残す
        value = re.sub(r'\[\[ファイル\:([^\]]+)\]\]', r'\1', value)
        # 内部リンク説明あり → 説明のみ残す
        value = re.sub(r'\[\[[^\]]+\|([^\]]+)]]', r'\1', value)
        # 内部リンク説明なし → リンク名のみ残す
        value = re.sub(r'\[\[([^\]]*?)]]', r'\1', value)
        basic_dic[field_name] = value

pprint(basic_dic)
