# 問題5
# ランダムに0から9までの値を10個出力しなさい．

import random

val = []
for i in range(10):
    val.append(random.randint(0, 9))

print(val)
