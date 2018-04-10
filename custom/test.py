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
        host1 = self.addHost( 'h1' )
	host2 = self.addHost('h2')
        host3 = self.addHost( 'h3' )
	host4 = self.addHost('h4')
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
	
        # Add links
        self.addLink( host1, switch1, 0, 1 )
        self.addLink( switch1, switch2, 3, 3)
        self.addLink( host2, switch1, 0, 2)
	self.addLink(host3, switch2, 0, 1)
	self.addLink(host4, switch2, 0, 2)

	#self.addLink( host1, switch1)
        #self.addLink( switch1, switch2)
        #self.addLink( host2, switch1)
	#self.addLink(host3, switch2)
	#self.addLink(host4, switch2)

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

