# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
list = []

with open('hightemp.txt') as f:
    for line in f:
        list.append(line.split('\t')[0])
        uniq = sorted(set(list), key=list.index)

with open('sort_uniq.txt', 'w') as f:
    for ken in uniq:
        f.write(ken + '\n')
