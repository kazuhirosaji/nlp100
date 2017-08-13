# 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
import sys
n = int(sys.argv[1])

f = open('hightemp.txt').readlines()
tail_n = len(f) - n

for key, line in enumerate(f):
    if key < tail_n:
        continue
    sys.stdout.write(line)