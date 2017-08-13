# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

import sys
n = int(sys.argv[1])

f = open('hightemp.txt', 'r')
for key, line in enumerate(f):
    if key >= n:
        break
    sys.stdout.write(line)
