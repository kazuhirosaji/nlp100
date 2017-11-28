# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
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
# ファイルの削除
base_info = re.sub(r'\[\[ファイル', "", base_info)
base_info = re.sub(r'\|.*?px\|', "", base_info)
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

