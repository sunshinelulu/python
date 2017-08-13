from wemePythonTest import getUserAvatar, emptyDir, avatarSavePath
from wemePythonTest import getRecommendUser, userToken, getTopicList,getActivitys
import time
import httplib, mimetypes
import json
def test_getUserAvatar():
	useId = range(3444, 3445)
	for i in useId:
		getUserAvatar(i)

def test_emptyAvatarDir(path):
	emptyDir(path)

def test_getRecommendUser(token):
	res = getRecommendUser(token)
	print res.read()

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





if __name__ == '__main__':
	path = 'C:\\Users\\lenovo\\Desktop\wemetest\\uploadAvatar\\1.jpg'
	tokenIn = '6bc80733304d173a19da94a24ede1117'
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
	
	