#-*- coding: utf8 -*-
#列表与字典的相关操作
L = [] 
print  L #原来不能在print语句中直接嵌套赋值等之类的子语句

L=[0,1,2,3]
print L

L = ['abc', [3,'dd']]

L = list('spam') 

L=list(range(-4, 4)) #前闭后开的这样的一个内容。

print L
print L[0]
print L[0:3]

print len(L)

LL = [1,2,3]

print LL + L #合并两个列表

print LL*3 #将列表扩充为3倍的长度

for x in LL:print x  #默认的print单个语句会打印出为一行的内容

print 3 in L #判断元素是否在某个列表之中
print 3 not in L 

L.append(4)
print L
L.extend([1,2,3])
print L
L.insert(0, 100) #插入，在指定的位置0拆入100，即为L[0]=100，之后数据往后延伸
print L
print L.count(100) #统计100在列表中出现的次数
L.sort() #调用排序之后，会改变L原来的内容
print L
L.reverse() #调用排序之后，会改变L原来的内容
print L

del L[3] #删除列表中的第三个元素，会影响列表原来的内容
del L[3:4]

print L
print L.pop() #把最后一个元素从列表中移除,并返回该值
print L
L.remove(2) #把元素2从列表中移除
print L
L.pop(0) #把下表为0的元素从列表中移除
L[2:4] = [66,66]
print L
LL = [x**2 for x in range(5)]
print LL
print list(map(ord, 'spam'))

print [1,2,3,4] + [4,5,6] #加法操作
print ['NI']*4
for x in [1,2,3]:
	print x , ' '
L = [3,2,7,6,0,1]
L.sort()  #默认的从小到大进行排序
L.sort(reverse=True)   #从小到达之后逆序排列
print L
print sorted(L), L #sorted(L)不会改变原来L的值
print list(reversed(L))#reversed(L)不会改变原来L的值

L*3   
print L#不会改变原来L的值
L2 = [3,4]
L + L2  #不会改变原来L的值
print L