# 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
count = 0
f = open('hightemp.txt', 'r')
for line in f:
    count += 1

print(count)
