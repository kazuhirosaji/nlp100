# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．
import nlp_json
import re

r = nlp_json.read_wikipedia()

# 文字列から[[Category:~]]を探す
list = re.findall('File\:.*?\|', r['revisions'][0]['*'])
# print(list)

# 余分な文字を削除
ans = []
for matched in list:
    ans.append(matched.replace('|', ''))

print(ans)