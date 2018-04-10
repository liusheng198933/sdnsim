from scapy.all import send, IP, TCP

if __name__ == '__main__':
	src = '10.0.1.0'
	dst = '10.0.1.8'
	pk = IP(proto=1,src=src,dst=dst)/TCP()
	send(pk)
