# 31. 動詞
# 動詞の表層形をすべて抽出せよ．
import analyze as gal
list = gal.get_analyzed_list()

verbs = []
for res in list:
    if (res['pos'] == '動詞'):
        verbs.append(res['surface'])

print(verbs)