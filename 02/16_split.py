# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
import sys
import math
n = int(sys.argv[1])

with open('hightemp.txt') as f:
    lines = f.readlines()

for key, line in enumerate(lines):
    if (key % n == 0):
        if (key != 0):
            out.close()
        out = open('split_' + str(math.floor(key / n)) + '.txt', 'w')
    out.write(line)
