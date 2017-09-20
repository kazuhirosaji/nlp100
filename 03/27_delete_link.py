# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
import nlp_json
import re
import regex

r = nlp_json.read_wikipedia()

# "{{基礎情報 ... }"の文字列の貪欲マッチ
list = re.findall('\{基礎情報[\s\S]*}', r['revisions'][0]['*'])

# {{基礎情報..}}の抽出のため、入れ子の括弧を正規表現で処理
# http://blog.ni-ken.net/2015/04/python-regex-tips/ 参照
pattern = r"(?<match>\{(?:[^{}]+|(?&match))*\})"
base_info = regex.search(pattern, list[0], flags=regex.VERBOSE).group('match')

# 強調マークアップの削除
base_info = re.sub(r'\'{2,5}', "", base_info)
# 内部リンクの削除
base_info = re.sub(r'\[\[|\]\]', "", base_info)

# 辞書オブジェクトを作成
ans = {}
for fields in base_info.split('\n|'):
    f = fields.split(' = ')
    if len(f) > 1:
        ans[f[0]] = f[1]

# 出力
for key, val in ans.items():
    print(key + ': ' + val)

