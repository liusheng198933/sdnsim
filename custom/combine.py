import numpy

def combineSeq(seq1, seq2, flow):
	newSeq = seq1
	if len(newSeq) == 0:
		for i in range(0, len(seq2)):
			newSeq.append([seq2[i], flow])
	else:
		j = 0
		for i in range(0, len(seq2)):
			while (j < len(newSeq)) and (newSeq[j][0] < seq2[i]):
				j = j + 1
			newSeq.insert(j, [seq2[i], flow])
	return newSeq
			
def poissonProcess(ld, maxTime):
		arrivalTime = []
#		for i in range(0,len(ld)):
#			arrivalTime.setdefault(i+1, [])
		ctime = numpy.random.exponential(1/ld)
		while ctime < maxTime:
			arrivalTime.append(ctime)
			ctime = ctime + numpy.random.exponential(1/ld)
		return arrivalTime	



if __name__ == '__main__':
	seq = []
	maxTime = 2
	flowPara = [0.7, 0.9, 0.8]
	for i in range(0, len(flowPara)):
		newS = poissonProcess(flowPara[i], maxTime)
		print(newS)
		seq = combineSeq(seq, newS, i+1)
	print(seq)
