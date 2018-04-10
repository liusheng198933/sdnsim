import subprocess
import time

def ping_response(host):
	ping_response = subprocess.Popen(["fping -c1 " + host], 					stdout=subprocess.PIPE,shell=True).stdout.read()
	print ping_response.strip().split()
	result = ping_response.strip().split()[5]
	return result

if __name__ == "__main__":
	#srcID = int(sys.argv[1])	
	#time.sleep(90)	
	print ping_response('10.0.1.8')
