#！coding:utf-8
import httplib, mimetypes
import urllib
import threadpool
import time
import os
import shutil
import json


avatarSavePath = 'C:\\Users\\lenovo\\Desktop\wemetest\\avatar\\'  #用户头像的存储地址
userCardPath = 'C:\\Users\\lenovo\\Desktop\wemetest\\userCard\\'  #用户卡片的存储地址
topicPath = 'C:\\Users\\lenovo\\Desktop\wemetest\\topic\\'
userToken = '6bc80733304d173a19da94a24ede1112'

def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be uploaded as files
    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = '----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = '\r\n'
    L = []
    for (key, value) in fields:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"' % key)
        L.append('')
        L.append(value)
    for (key, filename, value) in files:
        L.append('--' + BOUNDARY)
        L.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (key, filename))
        L.append('Content-Type: %s' % get_content_type(filename))
        L.append('')
        L.append(value)
    L.append('--' + BOUNDARY + '--')
    L.append('')
    body = CRLF.join(L)
    content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
    return content_type, body


def emptyDir(path):
	"""
		功能：检测目录是否存在，若存在则清空并创建目录
		主要用于项目中的存储的目录的清空，方便进行多次的测试
	"""
	if os.path.exists(path):
		shutil.rmtree(path)
	os.mkdir(path)

def uploadCommunityPost():
	pass

def uploadAvatar(tokenIn):
	"""
		功能：模拟用户上传头像的功能
	"""
	path = 'C:\\Users\\lenovo\\Desktop\wemetest\\uploadAvatar\\1.jpg'
	#tokenIn = '6bc80733304d173a19da94a24ede1117'
	fields = [('json', json.dumps({'number': '0', 'type':'0', 'token': tokenIn}))]
	content = open(path, 'rb').read()
	#decoded_content = content.decode('ISO-8859-1')
	files = [('avatar', 'file.jpg', content)]
	content_type, body = encode_multipart_formdata(fields, files)
	conn = httplib.HTTPConnection('121.248.51.210', 80)
	headers = {
		'Content-Type': content_type,
		'Host': '121.248.51.210:80',
		'Connection': 'Keep-Alive'}
	conn.request('POST', '/uploadavatar', body, headers)
	res=conn.getresponse()
	data = res.read()
	print data

def getActivitys(pageIn, tokenIn):
	"""
		功能：模拟首页的活动动能的压力测试
	"""
	conn = httplib.HTTPConnection('218.244.147.240', 8080)
	headers = {
		'Content-Type': 'application/json',
		'Host': '218.244.147.240:8080',
		'Connection': 'Keep-Alive'}
	params = json.dumps({'page': str(pageIn), 'token': tokenIn})
	conn.request('POST', '/getactivityinformation', params, headers)
	res=conn.getresponse()
	data = res.read()  #获取服务器返回的json信息
	temp = json.loads(data)
	if temp['state'] == 'successful':
		pass
	print data

def getTopicList(tokenIn):
	"""
	功能：对社区
	"""
	conn = httplib.HTTPConnection('218.244.147.240', 8080)
	headers = {
		'Content-Type': 'application/json',
		'Host': '218.244.147.240:8080',
		'Connection': 'Keep-Alive'}
	params = json.dumps({'token': tokenIn})
	conn.request('POST', '/gettopiclist', params, headers)
	res=conn.getresponse()
	data = res.read()  #获取服务器返回的json信息
	temp = json.loads(data)
	if temp['state'] == 'successful':
		topicList = temp['result']
		for topic in topicList:
			topicId = topic['id']
			topicImageURL = topic['imageurl']
			urllib.urlopen(topicImageURL) #其实我并不需要存储，只需要能够打开就可以了
			#urllib.urlretrieve(topicImageURL, topicPath + str(topicId)+'.jpg')

def getRecommendUser(tokenIn):
	"""
		APP寻觅功能的路由的模拟请求
		输入：用户的token
		输出：暂时不定
	"""
	#URL = '218.244.147.240'
	URL = '121.248.51.210'
	headers = {
		'Content-Type': 'application/json',
		'Host': URL + ':8080',
		'Connection': 'Keep-Alive'}
	params = json.dumps({'token': tokenIn})

	getRecommendUserStartTime = time.time()

	conn = httplib.HTTPConnection(URL, 8080)
	conn.request('POST', '/getrecommenduser', params, headers)
	res=conn.getresponse()

	getRecommendUserEndTime = time.time()

	data = res.read()
	temp = json.loads(data)
	if temp['state'] == 'successful':
		result = temp['result']
		firstRecommendUser = result[0]
		firstRecommendUserId = firstRecommendUser['id']
		firstRecommendUserAvatarURL = firstRecommendUser['avatar']
		#urllib.urlretrieve(firstRecommendUserAvatarURL, userCardPath + str(firstRecommendUserId)+'_card.jpg')
		#urllib.urlopen(firstRecommendUserAvatarURL)
		print "\nthe request is processed successfully!" + " user token is " + tokenIn + "\n"
	else:
		print "\nthe request failed!" + " user token is " + tokenIn + "\n"

	return getRecommendUserEndTime - getRecommendUserStartTime


def getUserAvatar(id):
	"""
		功能：对用户的头像进行请求的模拟脚本
	"""
	#URL = '218.244.147.240'
	URL = '121.248.51.210'

	getAvatarStartTime = time.time()

	conn = httplib.HTTPConnection(URL)
	conn.request('GET', '/avatar/'+str(id)+'_thumbnail.jpg')
	res=conn.getresponse()

	getAvatarEndTime = time.time()

	if res.status == 200:
		print "\nthe request is processed successfully!" + " user id is " + str(id)+ "\n"
		#data = res.read()
		#file = open(avatarSavePath + str(id)+'.jpg','w+b') 
		#file.write(data)  ##将得到的图片数据存储在本地。
		#file.close() 
	else:				
		print "\nthe request failed!" + " user id is " + str(id)+ "\n"
	#TODO:这里的结果还不是很美好，因为其实想要请求一个
	return getAvatarEndTime - getAvatarStartTime

def print_result(request, result):
	"""
		功能：线程池中的回调方法，对线程得到的结果进行处理
		暂时还不知道应该在这里放入什么方法
	"""
	#print result
	print "\nthis request spending time : ", result, '\n'

def exp_callback(request, exc_info):
    """
    	功能：异常发生时候调用的异常处理函数  
    """
    print exc_info

def run_threads(threadnum, func, args, callback=None):
    """
    	功能：用多线程进行并发请求
    	threadnum：线程池中的资源总数
    	func：线程所执行的方法
    	args：func的输入参数
    	callback：对func的结果进行处理
    """
    def exp_callback(request, exc_info):
    	"""
    		异常发生时候调用的异常处理函数  """
        print exc_info

    pool = threadpool.ThreadPool(threadnum)

    for req in threadpool.makeRequests(func, args, callback, exp_callback):
        pool.putRequest(req)

    while True:
        try:
            pool.poll()
        except KeyboardInterrupt:
            break
        except threadpool.NoResultsPending:
            break

    if pool.dismissedWorkers:
        pool.joinAllDismissedWorkers()

def test_getUserAvatar():
	"""
		功能：对用户头像的下载进行并发压力测试。
		或许不能叫做并发压力测试，因为根本就没有压到，纯粹就是负载测试。
	"""
	emptyDir(avatarSavePath)   #清空头像文件夹中已经存储的内容
	a = 20
	#b = 1416 #1400
	b = 1416
	argList = range(a, b)  #输入参数，存储的是用户的WEME ID
	print "the total Transactions numbers: ", b - a
	poolSize = 1000		#线程池中线程的个数
	pool = threadpool.ThreadPool(poolSize) #初始化一个线程池
	requests = threadpool.makeRequests(getUserAvatar, argList, print_result, exp_callback) #线程池运行所需要的参数
	
	startTime = time.time()

	for req in requests:
		pool.putRequest(req)
	pool.wait()

	endTime = time.time() 
	print "the task takes %s" % (endTime - startTime)

def test_getRecommendUser():
	"""
		功能：对寻觅的用户推荐功能进行压力测试
	"""
	emptyDir(userCardPath)  #清空用户的卡片的存储文件夹来进行本次的测试工作。
	a = 13213267367
	b = 13213268368
	#b = 13213267468
	tokenIntList = range(a, b)  #输入参数
	print "the total Transactions numbers: ", b - a - 1
	tokenStrList = [str(tokenInt) for tokenInt in tokenIntList]
	poolSize = 1000		#线程池中线程的个数
	pool = threadpool.ThreadPool(poolSize) #初始化一个线程池
	requests = threadpool.makeRequests(getRecommendUser, tokenStrList, print_result, exp_callback) #线程池运行所需要的参数
	startTime = time.time()

	for req in requests:
		pool.putRequest(req)
	pool.wait()

	endTime = time.time() 
	print "the task takes %s" % (endTime - startTime)

if __name__ == '__main__':

	#test_getUserAvatar()
	test_getRecommendUser()
