# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．
import analyze as gal
list = gal.get_analyzed_list()

ans = []
for res in list:
    if (res['pos'] == '名詞' and res['pos1'] == 'サ変接続'):
        ans.append(res)

print(ans)
