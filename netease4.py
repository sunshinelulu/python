from collections import deque
while True:
    try:
        n = int(raw_input())
        data = raw_input()
        dataList = data.split()
        dataInt = list(map(lambda s:int(s), dataList))
		
        prev = deque(maxlen=n)
        result = deque(maxlen=n)
        
       
        for i in dataInt:
        	prev.appendleft(i)
        	temp = prev
        	result.append(i)
        	prev = result
        	result = temp

        result = list(map(lambda s:str(s), result))
        print ' '.join(result)
    except:
        break