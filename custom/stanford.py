from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import Controller, OVSKernelSwitch, RemoteController

class MyTopod( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
	
        # Add hosts and switches
	for i in range(1, 241):
		self.addHost("h%s" %i)

	for i in range(1, 17):
		self.addSwitch("s%s" %i)

	for i in range(1, 30):
		self.addLink("h%s" %i, "s1", 0, i)

	for i in range(30, 46):
		self.addLink("h%s" %i, "s2", 0, i-29)

	for i in range(46, 60):
		self.addLink("h%s" %i, "s3", 0, i-45)
	
	for i in range(60, 73):
		self.addLink("h%s" %i, "s4", 0, i-59)

	for i in range(73, 78):
		self.addLink("h%s" %i, "s5", 0, i-72)

	for i in range(78, 83):
		self.addLink("h%s" %i, "s6", 0, i-77)

	for i in range(83, 108):
		self.addLink("h%s" %i, "s7", 0, i-82)

	for i in range(108, 132):
		self.addLink("h%s" %i, "s8", 0, i-107)

	for i in range(132, 143):
		self.addLink("h%s" %i, "s9", 0, i-131)

	for i in range(143, 154):
		self.addLink("h%s" %i, "s10", 0, i-142)

	for i in range(154, 165):
		self.addLink("h%s" %i, "s11", 0, i-153)

	for i in range(165, 176):
		self.addLink("h%s" %i, "s12", 0, i-164)

	for i in range(176, 182):
		self.addLink("h%s" %i, "s13", 0, i-175)

	for i in range(182, 188):
		self.addLink("h%s" %i, "s14", 0, i-181)

	for i in range(188, 238):
		self.addLink("h%s" %i, "s15", 0, i-187)

	for i in range(238, 241):
		self.addLink("h%s" %i, "s16", 0, i-237)

	self.addLink("s1", "s2", 30, 17)
	self.addLink("s1", "s3", 31, 15)
	self.addLink("s1", "s4", 32, 14)
	self.addLink("s1", "s5", 33, 6)
	self.addLink("s1", "s6", 34, 6)
	self.addLink("s1", "s7", 35, 26)
	self.addLink("s1", "s8", 36, 25)
	self.addLink("s1", "s9", 37, 12)
	self.addLink("s1", "s10", 38, 12)
	self.addLink("s1", "s11", 39, 12)
	self.addLink("s1", "s12", 40, 12)
	self.addLink("s1", "s13", 41, 7)
	self.addLink("s1", "s14", 42, 7)
	self.addLink("s1", "s15", 43, 51)
	self.addLink("s1", "s16", 44, 4)

	self.addLink("s2", "s3", 18, 16)
	self.addLink("s2", "s4", 19, 15)
	self.addLink("s2", "s5", 20, 7)
	self.addLink("s2", "s6", 21, 7)
	self.addLink("s2", "s7", 22, 27)
	self.addLink("s2", "s8", 23, 26)
	self.addLink("s2", "s9", 24, 13)
	self.addLink("s2", "s10", 25, 13)
	self.addLink("s2", "s11", 26, 13)
	self.addLink("s2", "s12", 27, 13)
	self.addLink("s2", "s13", 28, 8)
	self.addLink("s2", "s14", 29, 8)
	self.addLink("s2", "s15", 30, 52)
	self.addLink("s2", "s16", 31, 5)

	self.addLink("s3", "s4", 17, 16)
	self.addLink("s5", "s6", 8, 8)
	self.addLink("s7", "s8", 28, 27)
	self.addLink("s9", "s10", 14, 14)
	self.addLink("s11", "s12", 14, 14)
	self.addLink("s13", "s14", 9, 9)
	self.addLink("s15", "s16", 53, 6)
	
       
#topos = { 'mytopod': ( lambda: MyTopod() )

def simpleTest():
	topo = MyTopod()
	net = Mininet(topo=topo, switch=OVSKernelSwitch, controller=RemoteController)
    	

   	#c1 = net.addController('c1', controller=RemoteController, ip="127.0.0.1", port=6633)

	net.start()
	print "success!"
	CLI(net)
	net.stop()

if __name__ == '__main__':
	simpleTest()

