# 問題4
# ランダムに0から9までの値を10個出力しなさい．

import random

val = []

for i in range(10):
    r = random.randint(0,9)
    val.append(r)

print(val)
