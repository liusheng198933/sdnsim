import time
import numpy
from scapy.all import send, IP, TCP
import sys

class trafficInit():

	def __init__(self, hostID):
		#start_time = time.time()
		path = "/home/shengliu/Workspace/mininet/custom/controllerConfig.txt"
		self.flowPara = self.readFile(path, 8, 12)
		self.hostID = hostID
		am = 10
		self.maxTime = 1.5
		pkSeq = self.trafficGenerate(self.flowPara[self.hostID-1], self.maxTime)
		#fname = '/home/shengliu/Workspace/mininet/custom/data/result%d' %hostID
		#f = open(fname, 'w')
		if len(pkSeq) > 0:
			is_shown = 1
			#f.write('%d,%f,%d' %(1, self.flowPara[hostID-1], hostID));
		else:
			is_shown = 0
			#f.write('%d,%f,%d' %(0, self.flowPara[hostID-1], hostID));
		#f.close()
		print(is_shown)
		#print(self.hostID)
		#print("elapsed time is: %s ms" % (1000 * (time.time() - start_time)))
		self.trafficSend(pkSeq, self.hostID, am)
		#print("finish")
		#print is_shown

	def poissonProcess(self, ld, maxTime):
		arrivalTime = []
#		for i in range(0,len(ld)):
#			arrivalTime.setdefault(i+1, [])
		ctime = numpy.random.exponential(1/ld)
		while ctime < maxTime:
			arrivalTime.append(ctime)
			ctime = ctime + numpy.random.exponential(1/ld)
		return arrivalTime


	def combineSeq(self, seq1, seq2, flow):
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


	def trafficGenerate(self, flowPara, maxTime):
		#seq = []
		#for i in range(0, len(flowPara)):
		#	seq = self.combineSeq(seq, self.poissonProcess(flowPara[i], maxTime), i+1)
		#print flowPara

		seq = self.combineSeq([], self.poissonProcess(flowPara, maxTime), 1)
		return seq


	def trafficSend(self, seq, hostID, am):
		ptime = 0
		#print len(seq)
		for i in range(0, len(seq)):
			#print i
			#print (seq[i][0] - ptime) * am
			time.sleep((seq[i][0] - ptime) * am)
			pk = IP(proto=1,src=('10.0.1.%d'%(hostID-1)),dst='10.0.1.8')/TCP()
			send(pk)
			ptime = seq[i][0]
			#print ("pk sent, time: %f" % (seq[i][0] - ptime) * am)

	def readFile(self, path, flowNum, ruleNum):
		with open(path) as fp:

			for i in range(0, flowNum+2):
				fline = fp.readline().strip().split()

			fline = fp.readline().strip().split()
			intline = []
			for item in fline:
				intline.append(float(item))
			flowPara = intline

			fline = fp.readline().strip().split()
			flowInterest = int(fline[0])
			fline = fp.readline().strip().split()
			attackFlow = int(fline[0])

		return flowPara


if __name__ == '__main__':
#	print sys.argv
	trafficInit(int(sys.argv[1]))
