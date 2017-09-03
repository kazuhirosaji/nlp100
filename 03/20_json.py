# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．
import requests

def read_wikipedia():
    url = 'https://ja.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&titles=%E3%82%A4%E3%82%AE%E3%83%AA%E3%82%B9&rvprop=content'
    r = requests.get(url)
    page_id = sorted(r.json()['query']['pages'].keys())[0]
    print(r.json()['query']['pages'][page_id])

read_wikipedia()