import sys
import MeCab

m = MeCab.Tagger ("SNOW")
fin = open('neko.txt', 'r') # 解析対象のファイルを開く
fout = open('neko.txt.mecab', 'w') # 解析結果を書き出すファイルを開く
fout.write(m.parse(fin.read())) # 読み込んで解析して書き出し
fin.close() # ファイルを閉じる
fout.close()