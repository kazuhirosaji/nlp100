# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
# 品詞細分類1（pos1）をキーとするマッピング型に格納し，
# 1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，
# ここで作ったプログラムを活用せよ．

# surface pos,pos1,,,,base
# 吾輩  名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ

import sys
import MeCab
import re


def get_analyzed_list():
    m = MeCab.Tagger ("SNOW")
    list = []
    with open('neko.txt.mecab', 'r') as f:
        for line in f:
            arr = re.split('[,\t]', line.strip('\n'))
            if (len(arr) > 1):
                list.append({'surface' : arr[0], 'pos' : arr[1], 'pos1' : arr[2], 'base' : arr[-1]})

    # print(list)
    return list
