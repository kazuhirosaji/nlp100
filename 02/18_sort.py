# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
import sys

list = []
with open('hightemp.txt') as f:
    for line in f:
        tmp_list = line.split('\t')
        list.append(tmp_list)

list = sorted(list, key=lambda tmp: tmp[2])

with open('sort_tmp.txt', 'w') as f:
    for line_list in list:
        string = ''
        for key, cell in enumerate(line_list):
            if (key > 0):
                string += '\t'

            string += cell;
        f.write(string)
        # sys.stdout.write(string)
