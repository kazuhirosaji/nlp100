# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
import nlp_json
import re

r = nlp_json.read_wikipedia()

# 文字列から[[Category:~]]を探す
list = re.findall('\[\[Category:.*\]\]', r['revisions'][0]['*'])

# 余分な文字を削除
ans = []
for matched in list:
    matched = re.sub('Category:', "", matched)
    matched = re.sub('[\[\]\|\*]', "", matched)
    ans.append(matched)
    
print(ans)