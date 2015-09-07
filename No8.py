# 問題8
# 英単語が格納されているファイル(words.dat)を読み込みなさい． そして，英単語をランダムに出力しなさい．

import random

array = []

# ファイルから読み込む
f = open('words.dat', 'r')
for line in f:
    array.append(line.strip()) # strip() 文字列の先頭および末尾部分を除去したコピーを返す
f.close()

# まず，ランダムにリストの要素を決定
r = random.randint(0, len(array))
val = array[r]
print(val)

# しかし，要素の中身は，'番号 英単語 日本語訳'となっているので，英単語のみを取り出す
val = val.split()
word = val[1]
print(word)

# Pythonは文字列処理が超得意なんですね．

