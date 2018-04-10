import glob

def readFile(path, flowNum, ruleNum):
	with open(path) as fp:
		flowRule = {} #represents flow-rule relationship
		for i in range(0, flowNum):
			fline = fp.readline().strip().split()
			intline = []
			for item in fline:
				intline.append(int(item))
			flowRule[i] = intline
		rPrt = {} #record the priority of each rule, i.e. rPrt[rule] = priority
		for i in range(0, flowNum):
			for j in range(0, ruleNum):
				if flowRule[i][j] > 0:
					rPrt[j] = flowRule[i][j]

	#	print(rPrt)

		flowRuleTable = {} #flowRuleTable[flow] = rule
		for i in range(0, flowNum):
			flowRuleTable[i+1] = 0
			rp = 0
			for j in range(0, ruleNum):
				if flowRule[i][j] > rp:
					flowRuleTable[i+1] = j
					rp = flowRule[i][j]
			flowRuleTable[i+1] = flowRuleTable[i+1] + 1

		fline = fp.readline().strip().split()
		intline = []
		for item in fline:
			intline.append(int(item))
		ruleRd = intline

		fline = fp.readline().strip().split()
		intline = []
		for item in fline:
			intline.append(float(item))

		TTL = intline # TTL is a list
		ruleTable = {} # represents the ip and mask address, priority and TTL of each rule ruleTable[rule]
		ruleSrc = getRule()
		for i in range(0, ruleNum):
			ruleTable[i+1] = [ruleSrc[ruleRd[i]][0], ruleSrc[ruleRd[i]][1], rPrt[i], TTL[i]]

		fline = fp.readline().strip().split()
		intline = []
		for item in fline:
			intline.append(float(item))
		flowPara = intline

		fline = fp.readline().strip().split()
		flowInterest = int(fline[0])
		fline = fp.readline().strip().split()
		attackFlow = int(fline[0])

		return {'ruleTable': ruleTable, 'flowPara': flowPara, 'flowRuleTable': flowRuleTable, 'flowInterest':flowInterest, 'attackFlow': attackFlow}

def getRule():
	ruleSrc = {}
	ruleSrc[0] = ['10.0.1.0', '255.255.255.255']
	ruleSrc[1] = ['10.0.1.1', '255.255.255.255']
	ruleSrc[2] = ['10.0.1.2', '255.255.255.255']
	ruleSrc[3] = ['10.0.1.3', '255.255.255.255']
	ruleSrc[4] = ['10.0.1.4', '255.255.255.255']
	ruleSrc[5] = ['10.0.1.5', '255.255.255.255']
	ruleSrc[6] = ['10.0.1.6', '255.255.255.255']
	ruleSrc[7] = ['10.0.1.7', '255.255.255.255']
	ruleSrc[8] = ['10.0.1.0', '255.255.255.254']
	ruleSrc[9] = ['10.0.1.2', '255.255.255.254']
	ruleSrc[10] = ['10.0.1.4', '255.255.255.254']
	ruleSrc[11] = ['10.0.1.6', '255.255.255.254']
	ruleSrc[12] = ['10.0.1.0', '255.255.255.253']
	ruleSrc[13] = ['10.0.1.1', '255.255.255.253']
	ruleSrc[14] = ['10.0.1.4', '255.255.255.253']
	ruleSrc[15] = ['10.0.1.5', '255.255.255.253']
	ruleSrc[16] = ['10.0.1.0', '255.255.255.251']
	ruleSrc[17] = ['10.0.1.1', '255.255.255.251']
	ruleSrc[18] = ['10.0.1.2', '255.255.255.251']
	ruleSrc[19] = ['10.0.1.3', '255.255.255.251']
	ruleSrc[20] = ['10.0.1.0', '255.255.255.252']
	ruleSrc[21] = ['10.0.1.4', '255.255.255.252']
	ruleSrc[22] = ['10.0.1.0', '255.255.255.250']
	ruleSrc[23] = ['10.0.1.2', '255.255.255.250']
	ruleSrc[24] = ['10.0.1.0', '255.255.255.249']
	ruleSrc[25] = ['10.0.1.1', '255.255.255.249']
	ruleSrc[26] = ['10.0.1.0', '255.255.255.248']
	return ruleSrc

if __name__ == '__main__':
#	for fname in glob.glob("/home/shengliu/Workspace/sdnsim/data1/*.txt"):
	fname = "/home/shengliu/Workspace/sdnsim/data1/8_12para1_2.txt"
	result = readFile(fname, 8, 12)
	print result['ruleTable']
	print result['flowPara']
	print result['flowRuleTable']
	print result['flowInterest']
	print result['attackFlow']
