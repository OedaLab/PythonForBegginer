# 問題2
# キーボードから数値numを入力し，0からnumまでの偶数だけの和を求めなさい．

# 素朴な繰り返しで求める (while)
num = int(input("Input your number:"))

total = 0
i = 0
while i<=num:
    if i%2==0:
        total += i
    i += 1
print(total)
print()


# 偶数のみのリストを作って，リストの和を求める
array = list(range(0, num+1, 2))
total = sum(array)
print(total)
print()


# Pythonぽく求める
a = [i for i in range(num+1)]
b = [i for i in a if i % 2 == 0]
total = sum(b)
print(total)
print()
