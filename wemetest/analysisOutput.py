#-*- coding: UTF-8 -*- 

import re
ouputFilePath = 'C:\\Users\\lenovo\\Desktop\wemetest\\output.txt' 

global successTrans, failTrans, exceTrans, averageTaskTime,numTask, Transactions
successTrans = 0
failTrans = 0
exceTrans = 0
numTask = 0
averageTaskTime = 0
Transactions = 0
if __name__ == '__main__':
	outputFile = open(ouputFilePath) 
	for line in outputFile:
		if 'Transaction' in line:
			TransList = re.findall(r"\d+\.?\d*", line)
			print TransList
			Transactions = int(TransList[0])
		if 'successfully' in line:
			successTrans = successTrans + 1
		if 'spending' in line:
			numTask = numTask + 1
			timeList = re.findall(r"\d+\.?\d*", line)
			if len(timeList) > 0 :
				averageTaskTime = averageTaskTime + float(timeList[0])
		if 'failed' in line:
			failTrans = failTrans +1
		if 'exceptions' in line:
			exceTrans = exceTrans + 1
		if line is '':
			print "this is a empty line!\n"
	print "\n----------Analysis of the Loadtest---------\n"
	print "Transactions: " , Transactions
	print "successTrans: " , successTrans
	print "failTrans: " , failTrans
	print "exceTrans: " , exceTrans
	print "averageTaskTime: " , averageTaskTime/numTask
	print "success pecentage: ", float(successTrans)/float(Transactions)
