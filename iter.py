#-*-coding:utf-8-*-
#yield语句，使得用户自定义的函数可以转换为可迭代的生成器函数
def testIter():
	for i in range(10):
		yield(i)

#testIter() 调用之后就生成了一个迭代器，可以用list将其转换为一个列表包含了所有的对象
#print list(testIter())
t = iter(testIter())  #这一个步骤是一个必不可少的一步，表明使用迭代器协议进行元素的访问，才能使用下面的next的方法
print t.next() #0
print t.next() #1

#dir 可以当做一个帮助函数一样，看到可用的属性和方法
print dir(list)
