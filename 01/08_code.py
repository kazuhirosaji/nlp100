# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(msg):
    code = ''
    for s in msg:
        if (s.isalpha() and s.islower()):
            code += chr(219 - ord(s))
        else:
            code += s
    return code

print(cipher('I have an apple.'))
