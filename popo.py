#-*- coding: utf8 -*-
import json
import httplib
import string
#python的常常使用的代码片段

#这个是利用http请求来发送链接的一个东西
#GET 请求
try:
    conn = httplib.HTTPConnection("10.242.56.115",3000)
    conn.request("GET", "/api/versions?max_size=2")
    r1 = conn.getresponse()
    print r1.status, r1.reason
    print r1.read()
except Exception as e:
    print e
finally:
    conn.close()
    
#post请求
try:
    conn = httplib.HTTPConnection("www.baidu.com")
    name = 'lujuan'
    gender = 'female'
    data = {
        'name': name,
        'gender': gender
        }
    body = json.dumps(data)
    print body
    header = {"Content-type": "application/json"}
    conn.request("POST", "/api/versions", body,  header)
    r1 = conn.getresponse()
    #print r1.status, r1.reason
except Exception as e:
    print e
finally:
    conn.close()
    
#进行文件内容读写的一小段代码，模式和c语言中的文件的读写模式很相似
logfile = open("log.txt", "a+")
logfile.write(str(r1.status))
logfile.write("\r\n")
logfile.close()
if r1.status == 200:
    print "success"
#print r1.read()

#将http的body内容进行json化处理的一小段代码
#name对应的是一个list内容

a = '{"name":  [ {"id":"1"}, {"id":"2"}]   }'
#和name相对应的是一个list的东西,得到的内容要使用list对象的方式来处理
json_a = json.loads(a)
list_name = json_a['name']
for id in list_name:
    print id['id']

info = u'版本号：2.6.0\r\n描述：这是最新的一个版本\r\n\r\n'
print info.find(u'版本号：')
print info.find(u'描述：')
print info[4:11]

ls = string.split(info, u"\r\n")
ls_version = ls[0]
ls_detail = ls[1]
for l in ls:
    print l
    
#去除字符串中的前后的空格
a = "   help help   "
print a.strip()

#在python2.7中经常会用到的字符串编码的转换的工作，可以用如下的形式实现
s = u"hello world!"
s = s.encode('UTF-8')


#以空格分割字符串,并且指定分割的最多的个数是什么。
s = "      abcdef    dbcfget    dndnnnn  nnnnn  "
s = s.strip()
ll = string.split(s, maxsplit=2)

#将字符串转为整数，如果出错会怎么样？可以在这里测试一下
num1 = "7"
print int(num1)
try:
    num2 = "2.7.0"
    print int(num2)
except Exception as e:
    print e

#intro = versioninfo['versions'], 这样的json解析出错的时候的是
#会发出Exception这样的异常的因此就被捕获了，所以还要进一步的。

#python中逻辑非 and or not 似乎是支持者三种操作的。
result = True
print result
print not result
body = u"@BugEase bug 反馈信息 @BugEase bug "
body = string.replace(body, u"@BugEase", u"", 1)
body = string.replace(body, u"bug", u"", 1)
print body.strip()
    
        

