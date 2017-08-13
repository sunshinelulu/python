#-*- coding: UTF-8 -*- 
import MySQLdb
from wemePythonTest import uploadAvatar, uploadCommunityPost
#c.execute("SELECT id from users") #查询用户数据
#data = c.fetchall() #得到查询的结果
#print data #打印出数据
def createUsers():
	"""
		生成伪造的用户数据
	"""
	db = MySQLdb.connect(host="121.248.51.210",user="root",
                  passwd="lujuan19950329",db="flasktestdb", use_unicode=True, charset="utf8")
	c = db.cursor()
	for i in range(13213267768, 13213268768):
		if i % 2 == 0:
			gender = u"女"
		else:
			gender= u"男"
		values = [str(i),"fa31c410f3636ddce2bf1be73b66265f", str(i), u"东南大学", u"硕士", u"自动化", str(i), gender, u"南京"]
		c.execute("INSERT into users(username, password, token, school, degree, department, name, gender, hometown) values (%s, %s, %s,%s, %s, %s, %s, %s, %s)", values)
		db.commit()
		print i
	c.close()
	db.close()


def createUserAvatars():
	"""
		功能：上传很多用户的头像数据
	"""
	for tokenIn in range(13213267768, 13213268768):
		uploadAvatar(str(tokenIn))


def createCommunityPosts():
	"""
		功能：伪造很多的帖子数据
	"""
	pass

if __name__ == '__main__':
	#createUsers()
	createUserAvatars()