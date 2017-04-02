# 50个话题，案例场景+解决方案
##1. 数据结构
1.1 如何在列表、字典、集合中根据条件筛选数据
1.2 如何为元组中每个元素命名，提高程序可读性
1.3 如何统计序列中元素的出现频度
1.4 如何根据字典中值的大小对于字典中的项排序
1.5 如何快速找到多个字典的公共键(key)
1.6 如何让字典保持有序
1.7 如何实现用户历史记录保存（最多n条）





##2. 迭代器与生成器
2.1 如何实现可迭代对象和迭代器对象
2.2 如何使用生成器函数实现可迭代对象
2.3 如何进行反向迭代以及如何实现反向迭代
2.4 如何对迭代器做切片操作实现对于文本的切片操作?
**实际案例**
>有某个人文本文件，我们想读取某范围的内容：如100-300行之间的内容
,python中文本文件是一个可迭代对象，我们是否可以使用类似于列表切片
的方式得到一个100 - 300 行文件内容的生成器?
```
f = open('/var/mtianyan.txt')
f[100:300] #可以吗？
```

普通做法:
```python

f = open('guess.py')
# 'file' object has no attribute '__getitem__'
f[1:8]
print dir(f)


lines = f.readlines()

print lines[1:3]

# 使用seek操作使读取文件的游标返回到头部
f.seek(0)
for line in f:
    print line

```
高级做法:
```python
from itertools import islice

# print help(islice)

# islice(iterable, [start,] stop [, step])
# 
f = open('guess.py')
print islice(f, 1, 3)

# 打印一行到三行
for line in islice(f, 1, 3):
    print line
# 打印前3行
for line in islice(f, 3):
    print line
# 打印1到结尾
for line in islice(f, 1, None):
    print line
# 负不支持
# for line in islice(f, 1, -1):
#   print line

l = range(20)
print l

t = iter(l)

for x in islice(t,5,10):
    print x
print '*'*20
# 它会消耗迭代器对象，因此下面的for循环会从10开始
for x in t:
    print x

```


##3. 字符串处理

##4. 文件I/O操作

##5. 数据编码与处理

##6. 类与对象

##7. 多线程与多进程