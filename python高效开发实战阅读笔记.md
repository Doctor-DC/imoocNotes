[TOC]
##1. python基础知识
###1.1 菲波那切数列代码
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

def fbis(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

def main():
    result = fbis(10)
    fobj = open('result.txt', 'w+')
    for i, num in enumerate(result):
        print u"第 %d 个数是: %d" % (i, num)
        fobj.write("%d"%num)
        time.sleep(1)
    
if __name__ == '__main__':
    main()
```
###1.2 python中序列运算符：元素提取，序列链接
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = "Hello, I like Python Web Practice!"            
b = a[1]
                                    
b = a[7:13]                                 
print a[ :13]                               

print a[14:]                                

print "like" in a

print a + "!!"

print a

print "ABC" * 3

c = [2, 4, "apple", 5]                          
print c[1:]

print b + c[2]
```
###1.3 序列内置函数
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = [56, 2, 1, 893, -0.4]                   #列表类型
b = len(a)                                  #结果为 5
b = max(a)                                  #结果为 893
b = min(a)                                  #结果为 -0.4
print list(reversed(a)) 

print sorted(a)


```
###1.4 字符串基本使用演示
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

str1 = "Hello, World!"                          #普通字符串
str2 = u"Hello, I’m Unicode !"                  #Unicode字符串
str3 = u"你好，世界！"                        #Unicode字符串
print str2                                  #打印字符串
```
###1.5 所有sequence类型通用的切片操作可以读取字符串的部分内容
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

str1 = "Hello, World!"                          #定义字符串
print str1[5]                                 #位置为2的元素是逗号’,’          
print str1[7:]                              #读取位置从7到最后的子字符串
```