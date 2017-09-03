# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．
import sys
from collections import Counter

list = []
with open('hightemp.txt') as f:
    for line in f:
        list.append(line.split('\t')[0])

for key, val in Counter(list).most_common():
    print(val, key)
