#-*- coding: utf8 -*-
d={}
print type(d)
print dir(d)
#print help(dict)
d = {'b':1,
	  'a':2}
print d  #默认的会按照key组织排序起来

print len(d)
print 'b' in d



d['b'] = [1,2,3] #modify
d['c'] = [4,5,6] #add
del d['a']    #delete 删除字典中的某个元素
print d
print list(d.keys())
print list(d.values())
print list(d.items())
print d.get('d', 0) #利用get函数在找不到的时候增加一个默认值

dd = {'ee':3, 'dd' : 4}
d.update(dd)   #新加入元素在里面，合并两个字典
print d

print d.pop('b')  #删除键值为'b'的这样一个元素，并返回对应的值
print d

#python 字典创建的其他的形式
print dict(name='mel', age=45)
print dict([('name', 'mel'),('age', 45)])
print dict.fromkeys(['a', 'b'], 0)
print list(zip(['a', 'b', 'c'], [1,2,3]))
print dict(zip(['a', 'b', 'c'], [1,2,3]))
print {k:v for (k, v) in zip(['a', 'b', 'c'], [1,2,3])}
print {x : x **2 for x in [1,2,3,4]}