# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
import sys
f = open('hightemp.txt', 'r')
for line in f:
    sys.stdout.write(line.replace('\t', ' '))
