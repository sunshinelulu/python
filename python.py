#-*- coding:utf8-*-
#元组
p = (4, 5)
x, y = p
print x, y

#关于队列的知识
from collections import deque
a = deque(maxlen = 5)
a.append(3)  #在末尾加入元素
print a
a.appendleft(4) #在开头加入元素
print a
a.pop() #在尾部删除
a.popleft() #在头部删除
print a


#找出列表中的前n个最大值和最小值
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]


#math模块包的使用
import math
print math.pi, math.sqrt(4)
import random
print random.choice([1,2,3,5])
s = "hello"
a = slice(2,3) #前开后闭的这么一个区间
print s[a]
print s.find('h') #-1表示找不到，其他时候返回首次找到的下标
print s.replace('e', 'XYZ')

dd = [c * 2 for c in 'spam'] 
print dd #[ss, pp, aa, mm]

dict = {'b':1, 'a':2}
print dict.keys()
print sorted(dict)
print dict.get('x', 0)
if not 'x' in dict:
	print "miss" 

M = [[1,2,3], [4,5,6]]
print map(sum, M)

def fun(a):
	return True if len(a) > 3 else False
print filter(fun, M)  #很好用的一个过滤操作，可以把列表中符号要求的保留下来，不符合的去除掉

tt = (1,2,3,4)
print tt + (5,6)
print tt.index(4)
print tt.count(4)

f = open('data.txt', 'w')
f.write("hello")
f.close()
f= open('data.txt', 'r')
print f.read()
f.close()

#集合 操作
X = set('spam')
Y = {'h', 'a', 'm'}
print X
print X & Y
print X - Y
print X | Y

print type(X) #类型
print dir(X) #对象含有的属性和方法

print help(list.append) #查看list的append方法的使用帮助。

if type(X) == type(Y):
	print True
if type(X) == set:
	print True
print bool(X)
if isinstance(X, set):
	print True

print 0x123 #十六进制数字
print 0o12 #八进制数字
print complex(1, 1) #复数

print 3/2.0, 3 // 2.0 #除法， 以及只保留整数的除法

print math.trunc(2.5), math.floor(-2.5)
print oct(64), hex(64), bin(64)
print int('64'), int('100', 8), int('40', 16)
print '{0}, {1},  {2}'.format(1,2,3) #python中的格式化字符串
print '{0:o}, {1:x},  {2:b}'.format(64, 64, 64) #python中的格式化字符串X
print '%o, %x, %X' %(64, 255, 255)
a = set("ABCDE")
print 'A' in a
L = [1,3,2,1,3,2]
print list(set(L))
print ord('a')    #显示数值的大小 97

#单，双引号的区别
print 'we are\' family!', "we are\" family!", "we are\' family!","we are\' family!"
print "s\tp\na\x00m" #双引号和单引号中的\后面如果能够被转义，那么将按照转义字符来处理，如果不是合法
#的转义字符序列，那么将保留\,我们会看到结果中为\是不被转义的。
print 'C:\pa\pt'
print 'k' in 'hacker'
s = 'spamm'
print s[1:3], s[:-1], s[0:] #连slice列表中的都是前闭后开的一个区间，所以-1是被排除在外的
print s[1:3:1] #前闭后开，在1，2两个元素中以step为1的步进来获得元素
print str(2)
s = 'spa   aam   uuu'
print s.split()
print s.find('aam')
print s.rstrip()
print s.strip()
print s.replace('a', 'bb')

print '%(n)d is a %(m)s' %{"n":3, "m":"she is a dog!"}
print type({1,2,3})


""" #*号在迭代器中的神奇的作用,这个估计是3.0的python所支持的语法
def sum(items):
	head, *tail = items
	return head + sum(tail) if tail else 
print sum([1,2,3]) """

#
#with ... as ....
#yield 生成器函数