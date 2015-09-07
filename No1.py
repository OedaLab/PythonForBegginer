# 問題1
# 1から10までの和を求めなさい．


# 素朴な繰り返しで求める (for)
total = 0
i = 0
while i<=10:
    total += i
    i += 1
print(total)
print()


# 素朴な繰り返しで求める (for)
total = 0
for i in range(10):
   total += i+1
print(total)
print()


# リストを使ってみる
array = list(range(11))
total = sum(array)
print(total)
print()


# リスト内包表記
array = [i for i in range(11)]
total = sum(array)
print(total)
print()
