# -*- coding: utf-8 -*-
# # 1-通用做法
# data = [1,2,3,4,5,6,7,8]
# res = []
# for x in data:
#     if x >= 2:
#     	res.append(x)
# print res

# # 2-高级:(函数式编程/列表解析/字典解析/集合解析)
# #函数式编程
# res = filter(lambda x:x>=2,data)
# print res
# #列表解析
# res = [x for x in data if x>=2]
# print res
# #字典解析
# dic = {'a':23,'b':98,'c':0}
# res = {k:v for k,v in dic.iteritems() if v>90}
# print res
# #集合解析
# s = (1,2,3,4,5,6,7,8)
# res = {x for x in data if x>=2}
# print res



# # example1 列表解析
# from random import randint
# #使用列表解析生成10个元素
# data = [randint(-10,10) for _ in xrange(10)]
# print data
# #filter(func,sequence)
# res = filter(lambda x:x>=0,data)
# print res
# # 列表解析
# res = [x for x in data if x>=0]
# print res
# #Time: filter&列表解析
# #>>>代表在ipython下
# #>>> timeit filter(lambda x:x>=0,data)
# #>>> timeit [x for x in data if x>=0]
# # 结果：列表解析：432ns(纳秒)
# # 		filter  ：1.4us(微秒)=1400ns
# # 		1微秒等于1000纳秒
# res = [x for x in data if x>=0]
# print res


# # example2 字典解析
# from random import randint
# # 某班有20个人，分数分布在60~100
# d = {x: randint(60,100) for x in xrange(1,21) }
# print d
# print { k for k in d if k>10}
# print {v for v in d.values() if v>90}
# print {k for k in d.keys() if k>10}
# res = {k:v for k,v in d.iteritems() if v>90}
# print res


# # 集合解析
# from random import randint
# data = [randint(-10,10) for _ in xrange(10)]
# s = set(data) 
# print s
# sres = {x for x in s if x % 3 == 0}
# print sres

# student = ('mtianyan',18,'male','1147727180@qq.com')

# # name
# print student[0]

# # age 
# print student[1] >= 10;

# # sex
# print student[2] == 'male'

# from random import randint

# # #使用列表解析生成30个元素(在0~20范围内)
# data = [randint(0,20) for _ in xrange(30)]
# print type(data)

# # 使用列表创建字典.data为key值，value为0
# c = dict.fromkeys(data,0)
# print c

# # 使用for循环遍历data,遇到一个x，计数器c[x]就会增加1
# for x in data:
# 	c[x] +=1
# print c
# c1= {k:v for k,v in c.iteritems()}
# print c1

# #根据字典的值对于字典的项进行排序
# stat = sorted(c.iteritems(),key= lambda d:d[1],reverse=True)
# print stat

# # example1 使用Counter
# from collections import Counter

# c2 = Counter(data)

# #传入需要几个数值
# smax = c2.most_common(5)
# smin = c2.most_common()[:-6:-1]
# print smax
# print smin

# import re

# txt = open('code.txt').read()

# # print txt

# # 分割词:通过非字母字符
# word = re.split('\W*',txt)

# # print word

# from collections import Counter
# c3 = Counter(word)
# # print c3

# print c3.most_common(10)


# a = sorted([9,1,2,8,5])
# print a

# # 按值对字典排序
# # 

# from random import randint

# #使用字典解析创建成绩表
# dic = { x:randint(60,100) for x in 'abcdefg'}
# print dic

# skey = sorted(dic)
# print skey

# print iter(dic)
# print list(iter(dic))

# # 将字典进行转换变成sorted可以排序的

# print (97,'a') > (69,'b')
# print (97,'a') > (97,'b')

# print dic.keys()
# print dic.values()
# print zip(dic.keys(),dic.values())

# #进行优化内存使用可迭代对象
# print zip(dic.itervalues(),dic.iterkeys())

# print sorted(zip(dic.itervalues(),dic.iterkeys()))


# ###利用sorted的key传值
# # sorted 传入三个参数：
# # 1. 一个可迭代的对象 
# # 2：key值：这里传入一个lambda匿名函数。取出每个迭代项的values
# # 3：reverse：正序还是倒序：默认为False从小到大

# print dic.items()

# # 从小到大排列
# print sorted(dic.items(), key=lambda x:x[1])
# # 从大到小排列
# print sorted(dic.items(), key=lambda x:x[1],reverse =True)

# ##优化内存版本

# # 从小到大排列
# print sorted(dic.iteritems(), key=lambda x:x[1])
# # 从大到小排列
# print sorted(dic.iteritems(), key=lambda x:x[1],reverse =True)
# 
# 
# from random import randint, sample
# # 随机取样出3到5个
# persons = sample('abcdefg',randint(3,6))

# dic1 = {k:randint(0,5) for k in persons}
# dic2 = {k:randint(0,5) for k in persons}
# dic3 = {k:randint(0,5) for k in persons}

# res = set()
# # 遍历dic1的key。
# # 如果dic2与dic3中也有这个key，将其保存进res
# for k in dic1:
# 	if k in dic2 and k in dic3:
# 		res.add(k)
# print res

# ###解决方案

# #利用集合(set)的交集运算
# # 1. 利用字典的viewskeys()方法，得到一个字典keys的集合
# # 2. 利用map函数，得到所有字典的keys的集合
# # 3. 使用reduce函数，取所有字典的keys的集合的交集

# # 利用字典的viewskeys()方法，得到一个字典keys的集合
# print type(dic1.viewkeys())

# print dic1.viewkeys() & dic2.viewkeys() & dic3.viewkeys()

# # 利用map函数，得到所有字典的keys的集合解决n轮比较

# worklist =[dic1,dic2,dic3]
# print map(dict.viewkeys,worklist)

# print reduce(lambda a,b:a & b,map(dict.viewkeys,worklist))


# d = {}

# d['Jim'] = (1,35)
# d['Leo'] = (2,37)
# d['Bob'] = (3,40)

# # for k in d:print k
# # 由结果可以发现默认数据结构dict，没有顺序

# #解决方案：
# # 使用collections.OrderedDict
# # 以OrderedDict代替内置字典dict，依次将选手成绩存入OrderedDict

# # from collections import OrderedDict

# # d2 = OrderedDict()
# # d2['Jim'] = (1,35)
# # d2['Leo'] = (2,37)
# # d2['Bob'] = (3,40)

# # for k in d2:print k

# # 编程模拟竞赛系统：
# from time import time
# from random import randint
# from collections import OrderedDict

# d = OrderedDict()
# palyers = list('abcdefg')

# start = time()
# # print start

# for i in xrange(7):
# 	# 延时
# 	raw_input()
# 	# 每次随机选取一名选手答题完毕
# 	p = palyers.pop(randint(0, 6 - i))
# 	end = time()
# 	print i + 1,p, end - start
# 	d[p] =(i+1,end-start)

# #比赛结束打印成绩

# # 打印换行
# print 
# # 打印分隔符
# print '-'*20

# for k in d:
# 	print k,d[k]
# 	

# # 使用队列

# from collections import deque

# # deque传入两个参数:1.初始值;2.队列长度
# q = deque([],5)

# # append方法从右部添加
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4)
# q.append(5)
# q.append(6)

# print q

# from collections import deque
# from random import randint

# Num = randint(0,100)
# history = deque([], 5)

# def guess(k):
# 	if k == Num:
# 		print "success"
# 		return True
# 	elif k > Num:
# 		print "the number is bigger"
# 	else:
# 		print "the number is smaller"
# 	return False

# while True:
# 	line = raw_input("please input a number(1~100)哈哈:")
# 	if line.isdigit():
# 		k = int(line)
# 		history.append(k)
# 		if guess(k):
# 			break
# 	elif line == 'history' or line == 'h?':
# 		print list(history)
# 	else:
# 		print 'input error'
# q = deque([3,4,5,6,7])

# # 将对象存储进文件进行持久化
# import pickle

# pickle.dump(q,open('history','w'))

# q2 = pickle.load(open('history'))
# print q2

from random import randint
math = [randint(60,100) for _ in xrange(40)]
english = [randint(60,100) for _ in xrange(40)]

for i in xrange(len(math)):
	print math[i] + english[i]

# zip 

print zip([1,2,3],['a','b','c'],[7,8,9])
# out:[(1, 'a', 7), (2, 'b', 8), (3, 'c', 9)]

for m,e in zip(math,english):
	print m+e

from random import randint
from itertools import chain
c1 = [randint(60,100) for _ in xrange(40)]
c2 = [randint(60,100) for _ in xrange(42)]
count = 0
for s in chain(c1,c2):
	if s > 90:
		count +=1
print count