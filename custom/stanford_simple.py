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
	for i in range(1, 60):
		self.addHost("h%s" %i)

	for i in range(1, 4):
		self.addSwitch("s%s" %i)

	for i in range(5, 30):
		self.addLink("h%s" %i, "s1", 0, i)

	for i in range(30, 46):
		self.addLink("h%s" %i, "s2", 0, i-29)

	for i in range(46, 60):
		self.addLink("h%s" %i, "s3", 0, i-45)
	

	self.addLink("s1", "s2", 30, 17)
	self.addLink("s1", "s3", 31, 15)
	
	self.addLink("s2", "s3", 18, 16)
	
	self.addSwitch("s101")
	self.addLink("h1","s101", 0, 1)
	self.addLink("h2","s101", 0, 2)
	self.addLink("h3","s101", 0, 3)
	self.addLink("h4","s101", 0, 4)
	self.addLink("s1","s101", 1, 5)

	
       
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

