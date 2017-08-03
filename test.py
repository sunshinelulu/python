

while True:
	try:
		input = raw_input()
		L = input.split()
		#L = string.split(input)
		intL = map(lambda x:int(x), L)
		print intL
	except:
		break