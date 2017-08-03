#-*- coding: utf8 -*-
##为了能够在python2.6的版本中使用python3的特性的一种方法
#from __future__ import print_function  


out = open(r'test.txt', 'w') #'w'代表输出并生成一个文件
out.write('hello\n')
out.write('hellohello\n')
out.write('hellohellohello\n')

L = ['lujuan', 'luhang']
out.writelines(L)  #好像并没有什么分隔符这样子，将列表中的所有的内容输出到文件中

out.flush() #刷新输出缓冲区，将缓冲区中内容输出到文件中，但并不关闭文件

out.close()  #原来close函数还真是必不可少的一个东西，简直不能忍受。

infile = open(r'test.txt', 'r')

c = infile.read()  #把整个文件读进单一的字符串中
print c
infile.close()

infile = open(r'test.txt', 'r')
cN = infile.read(3)  #infile 将该指针向前推进了三个字符
print cN

line1 = infile.readline() #infile 继续读取之后的几个字符，所以文件的指针的位置真的是蛮重要的。
print line1

infile.seek(0)  #修改文件位置到某一个偏移的地方
lines = infile.readlines()  #按照每一行每一行的遍历进行打印输出
for line in lines:
	print line

fb = open('data.bin', 'wb')
fb.write('%s' % 115)
fb.close()

fb = open('data.bin', 'rb')  #将字符串转为python对象 eval
print eval(fb.read())  #使用eval函数可能有时候会过分的解读文件中的内容
fb.close()

#pickle 库存储和逆序列python对象
import pickle
#shelve 也是一个按键存储的比较好的使用工具
import shelve

#IO重定向，python中提供了比较方便的IO重定向的方法。
log = open('log.txt', 'a')
print >> log, 'hellohellohello\n','hellohellohello\n'
log.close()


print ('python 3 print_function')