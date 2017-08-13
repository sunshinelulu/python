
from collections import deque
while True:
    try:
        data = raw_input()
        dataList = data.split()
        (x, f, d, p) = list(map(lambda s:int(s), dataList))
        if d/x <= f:
        	result = d/x
        else:
        	result = (d + f *p)/(p + x)
        print result
    except:
        break
