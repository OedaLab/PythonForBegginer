# BeginnerForPython
C言語は知っているがPythonは全く知らない人を対象として，最速でPythonを修得するチュートリアルです．
Pythonの対象バージョンは3.4.3です．

# ipythonでPythonに慣れる
## ipythonの起動
コマンドラインから以下のように入力

```
$ ipython
```

すると起動する．

```
In [1]:
```

これがプロンプトになる．
ここから以下のチュートリアルを行っていく．

## 変数と標準出力
C言語と同じで左辺を右辺に代入する．

違う点は，変数宣言がない．行末に;（セミコロン）が要らない．

```
a = 4
b = 5
total = a + b
print(total)
print(a, b, total)
print("a=", a, ", b=", b, "total=", total)
print("a=%d, b=%d, total=%d" %(a, b, total))
```
すごく便利なのが，ipythonのプロンプトで変数名を入力すると値が表示される．
```
total
a+total
```

### 使えない変数名
str, sumなどは予約語，組み込み関数名なので使うと上書きしてしまう．
使えるように見えてしまう点にも注意が必要である．
使えない変数名は最下部に掲載する．
ここでは，つい使ってしまうが実は使えない変数名を掲載する．
```
str, sum, max, min, lambda, input, next set, type all, any, bin, dir, len, range, round, vars
```

## 繰り返し
繰り返しは```while```と```for```がある．

### while
まず```while```から説明する．大きな注意点が2つある．

注意1. Pythonでびっくりするのが，while, if, 関数などのブロックを表すとき，{ } などの括弧ではなく，タブを使う．
注意2. インクリメントはない．つまり，```a++```はできない．```a += 1```と記述する．
```
a = 0
while a<3:
  print(a)
  a += 1
```

### for
```
a = 0
for i in range(3):
  a += i
```

range(3)で0,1,2までカウントする．

## リスト
Pythonには配列はない．代わり，それよりも便利なリストがある．リストを配列のように使えばよい．

```
a = [4, 6, 65]
a[0]
a[1]
```
のように使える．

リストには何でも格納できる．型もばらばらでもよい．
```
a = [4, 6, 65, "hoge", ]
a[2]
a[3]
```

リストにリストを格納することもできる．これで多次元配列を実現できる．
```
a = [[1,2,3], [4,5,6]]
a[0]
a[0][1]
```

リストとforの組み合わせが最強である．
```
a = [10,20,30,40,50]
for i in a:
  print(i)
```

先ほどの```range()```は，連番を作ることができる．
```
list(range(3))
list(range(8, 23))
list(range(10, 20, 2))
```

# ファイルの書き込んだプログラムを起動する．
適当なファイル(example1.py)を開き，以下のように記述して保存する．
```
a = 123
b = 456
c = a + b
print(c)
```
そして，```ipython```では，
```
In [1]: %run example1.py
```
のように```%run```で呼び出す．
呼び出した後も，変数にアクセスできるため，値の確認に便利．

### 問題1 (No1.py)
1から10までの和を求めなさい．
[解答](./No1.py)

## 文字列
```
a = "Hello World"
print(a)
```

## キーボード入力，そして出力
キーボードから数値を入力すれば数値に，文字列を入力すれば，格納後の変数は適切に型変換される．
```
a = input()
print(a)
```

キャストは次のようになる．
```
a = input()
(453と数値を入力したつもりでも，デフォルトは"453"という文字列である．)
b = int(a)

a = 987
(987と文字列を入力したつもりでも，987という数値である．)
b = str(a)
```

## if文
```
a = int(input())
if a==1:
  print("One")
elif a==2:
  print("Two")
else:
  print("Others")
```

### 問題2 (No2.py)
キーボードから数値numを入力し，0からnumまでの偶数だけの和を求めなさい．
[解答](./No2.py)


### 問題3 (No3.py)
キーボードから文字列を入力して，その文字列の長さをカウントしなさい．
[解答](./No3.py)


### 問題4 (No4.py)
キーボードから文字列を2つ入力して，それを結合して出力しなさい．
[解答](./No4.py)


## 乱数
```
import random

random.seed(1) # 乱数の種を1で初期化．この1行がない場合，乱数の種はUNIX秒を初期値とする．
r = random.random() # 0.0～1.0までのfloat型の値を取得する．
r = random.randint(x,y) # xからyまでのint型の値を取得する．

array = list(range(0,10))
random.shuffle(array) # リストをランダムに並び替える．
```

ちなみに，
```
array.sort()
```
で並び替えてくれる．

### 問題5 (No5.py)
ランダムに0から9までの値を10個出力しなさい．
[解答](./No5.py)

### 問題6 (No6.py)
ランダムに英小文字を10個出力しなさい．
[解答](./No6.py)

## 関数
関数は書き方がC言語と違うだけで，使い方は一緒．

```
def func(x):
  y = x*100
  return y

num = 123
ans = func(num)
print(ans)
```

しかも，複数の戻り値を返すことができる．
```
def func(x):
  y = x*100
  z = x*2
  return y, z

num = 123
ans1, ans2 = func(num)
print(ans1, ans2)
```

### 問題7（No7.py)
英文の単語の数をカウントしなさい．例えば
In order to stay healthy, you should have a balanced diet and get regular exercise.
では，単語数は15個となる．
[解答](./No7.py)

## ファイル入力
```
f = open('data.dat', 'r')

for line in f:
    print(line, end='')
f.close()
```
### 問題8（No8.py)
英単語が格納されているファイル(words.dat)を読み込みなさい．
そして，英単語をランダムに出力しなさい．
[データ](./words.dat)

# 使えない変数名の一覧
## 予約語
```
>>> __import__('keyword').kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
## 組み込み関数名
```
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError',
'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis',
'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError',
'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopIteration', 'SyntaxError',
'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError',
'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__',
'__name__', '__package__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes',
'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr',
'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format',
'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int',
'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max',
'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted',
'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```
