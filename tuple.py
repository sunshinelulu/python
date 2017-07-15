#-*- coding: utf8 -*-
#pyhton 中万物皆为对象
#print 3.str()
t = ()
t = (0, )
t = (0, 'Ni', 1.2, 3)
t = 0, 'Ni', 1.2, 3
t = ('abc', ('def', 'ghi'))
t = tuple('spam')
print t, t[0], t[1:3], len(t)
t2 = (1,2,3,4,2)



print t + t2, t #不会改变原来t的值
print t*3, t    #不会改变原来t的值 

for x in t:print x
print [x *2 for x in t]

print t.index('s')

print t.count('s')

tmp = list(t)
tmp.sort()
print tmp

tt = tuple(tmp)
print sorted(tt)
print t2.index(2) #2第一次出现的下标
print t2.index(2,3)#在3下标之后（包括3），2第一次出现时的下标
print 2 in t2