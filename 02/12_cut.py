# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
import sys
f = open('hightemp.txt', 'r')
col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')
for line in f:
    words = line.split('\t')
    col1.write(words[0] + '\n')
    col2.write(words[1] + '\n')
