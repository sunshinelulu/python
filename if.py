#-*- coding: utf8 -*-
#if语句的跨越多行的写法1
if 1 == 2 and 3 > 4 or \
	5 == 6:
	print True
else:
	print False

#if语句的跨越多行的写法2
if (1 == 2 and 3 > 4 or 
	5 == 6):
	print True
else:
	print False

#python中逻辑运算符为 and or not
##python中的if语句在终极剪短版本
result = 1 if True else 2

i = 0
while i < 3:  #while也可以和else搭配，当while正常结束，没有break的时候
	print i   #时候就会执行else语句中的内容，真的是很正常的一个内容
	i = i + 1
else:
	print i

#range函数的优雅的用法
print range(0, 10, 2)
print range(5, -5, -1)
print range(10)

#zip函数能够让我们能够并行的在for循环中遍历多个序列
L1 = [1,2,3,4]
L2 = [5,6,7,8]
L3 = [1,2,3,4]
for x, y, z in zip(L1, L2, L3): #打印出：1,5,1
	print x , y,z                       #2,6,2

#map通常将一个函数应用在一个列表和集合中的每个元素上的一个操作
#使用zip来构造字典结构
key = [1,2,3]
values = ['a', 'b', 'c']
print dict(zip(key, values))

#enumerate 产生元素的以及元素的便宜
s = 'hellohellohello'
for (offest, element) in enumerate(s):
	print offest ,':' , element
