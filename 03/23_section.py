# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
import nlp_json
import re

r = nlp_json.read_wikipedia()

# 文字列から[[Category:~]]を探す
list = re.findall('\==.*\==', r['revisions'][0]['*'])
print(list)

# 余分な文字を削除
ans = []
for matched in list:
    level = matched.count('=') / 2 - 1
    ans.append([matched.replace('=', ''), int(level)])

print(ans)