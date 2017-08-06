# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
import sys
f1 = open('col1.txt', 'r')
f2 = open('col2.txt', 'r')

m = open('13merged.txt', 'w')
for (col1, col2) in zip(f1, f2):
    m.write(col1.rstrip('\r\n') + '\t' + col2.rstrip('\r\n') + '\n')
