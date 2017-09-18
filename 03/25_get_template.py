# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ
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

# 辞書オブジェクトを作成
ans = {}
for fields in base_info.split('\n|'):
    f = fields.split(' = ')
    if len(f) > 1:
        ans[f[0]] = f[1]

# 出力
for key, val in ans.items():
    print(key + ': ' + val)
