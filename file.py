#-*- coding: utf8 -*-
out = open(r'test.txt', 'w')
out.write('hello\n')

out.close()  #原来close函数还真是必不可少的一个东西，简直不能忍受。

infile = open(r'test.txt', 'r')

c = infile.read()  #把整个文件读进单一的字符串中
print c
infile.close()

infile = open(r'test.txt', 'r')
cN = infile.read(3)  #infile 将该指针向前推进了三个字符
print cN

line1 = infile.readline() #infile 继续读取之后的几个字符
print line1

infile.seek(0)
lines = infile.readlines()
print lines