# 問題7
# 英文の単語の数をカウントしなさい．例えば In order to stay healthy, you should have a balanced diet and get regular exercise. では，単語数は15個となる．

st = input('Input your sentense=')

# 素朴に作る
wordCount = 0
i = 0
while i<len(st):
    if st[i] == ' ':
        wordCount += 1
    i += 1

wordCount += 1
print(wordCount)
print()

# しかし，不十分．
# いろいろエラー処理が大変


# pythonぽく作る
wordCount = len(st.split())
print(wordCount)
print()
