#--*--coding:utf-8--*--

class someClass:

	def __init__(self):
		self.name = "lujuan"
		self.day = "time"

obj = someClass()
obj2 = someClass()

#在python中进行对象的存储和反存储的。只要用pickle就可以了
import pickle
file = open('pickleFile', 'wb')
pickle.dump(obj, file)
pickle.dump(obj2, file)
file.close()

file = open('pickleFile', 'rb')
while True:
	try:
		obj = pickle.load(file)
		print obj.name
		print obj.day
	except:
		print "end!"*3
		file.close()
		break

#shelv 也是进行对象存储的，不过就是使用的key和value的方式进行的存储
import shelve

obj = someClass()
dbbase = shelve.open("shelveFile")
dbbase['key'] = obj

#根据key来进行对象的提取和操作，但是其实这个还是不方便的，因为不知道到底class中有什么样的对象
newObj = dbbase['key']
print newObj.name
print newObj.day

