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
2.5 如何在一个for语句中迭代多个可迭代队象(并行&串行)？
实际案例:
>1. 某班学生期末考试成绩，语文，数学，英语分布存储在三个列表当中
    同时迭代三个列表，计算每个学生的总分
2. 某年级有四个班，某次考试每班英语成绩分布存储在4个列表中，依次迭代每个列表，统计全年级成绩高于90分的人

解决方案:
> 并行，采用内置函数zip，它能将多个长度一样的可迭代对象合并，每次迭代返回一个元组
串行，采用标准库里的itertools.chain，它能将多个可迭代对象链接

普通做法:
```python

from random import randint
math = [randint(60,100) for _ in xrange(40)]
english = [randint(60,100) for _ in xrange(40)]

for i in xrange(len(math)):
    print math[i] + english[i]

```
zip实现并行迭代
```python
from random import randint
math = [randint(60,100) for _ in xrange(40)]
english = [randint(60,100) for _ in xrange(40)]
# zip 

print zip([1,2,3],['a','b','c'],[7,8,9])
# out:[(1, 'a', 7), (2, 'b', 8), (3, 'c', 9)]

for m,e in zip(math,english):
    print m+e
```
itertools.chain实现多个可迭代对象的链接
```python
from random import randint
from itertools import chain
c1 = [randint(60,100) for _ in xrange(40)]
c2 = [randint(60,100) for _ in xrange(42)]
count = 0
for s in chain(c1,c2):
    if s > 90:
        count +=1
print count
```

##3. 字符串处理

##4. 文件I/O操作

##5. 数据编码与处理

##6. 类与对象

##7. 多线程与多进程