# 32. 動詞の原形
# 動詞の原形をすべて抽出せよ
import analyze as gal
list = gal.get_analyzed_list()

verbs = []
for res in list:
    if (res['pos'] == '動詞'):
        verbs.append(res['base'])

print(verbs)
