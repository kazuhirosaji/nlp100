# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
# その実行結果を確認せよ．

import random

def typoglycemia(sentence):
    res = ''
    for word in sentence.split():
        if (len(res) > 0):
            res += ' '
        new_word = ''
        if (len(word) > 4):
            # 並び替え順を決定
            rep_list = list(range(1, len(word) - 1))
            random.shuffle(rep_list)
            # 先頭と最後尾はそのままにする
            rep_list.insert(0, 0)
            rep_list.append(len(word) - 1)

            for key, str in enumerate(word):
                new_word += word[rep_list[key]]
        else:
            new_word = word

        res += new_word
    return res

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
res = typoglycemia(sentence)
print(sentence)
print(res)