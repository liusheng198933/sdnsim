from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from time import sleep

class MyTopod( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost('h1', ip='10.0.1.0')
        host2 = self.addHost('h2', ip='10.0.1.1')
        host3 = self.addHost('h3', ip='10.0.1.2')
        host4 = self.addHost('h4', ip='10.0.1.3')
        host5 = self.addHost('h5', ip='10.0.1.4')
        host6 = self.addHost('h6', ip='10.0.1.5')
        host7 = self.addHost('h7', ip='10.0.1.6')
        host8 = self.addHost('h8', ip='10.0.1.7')
        host9 = self.addHost('h9', ip='10.0.1.8')


        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's100' )
        #switch4 = self.addSwitch( 's101' )

        # Add links
        self.addLink(host1, switch3, 0, 1)
        self.addLink(host2, switch3, 0, 2)
        self.addLink(host3, switch3, 0, 3)
        self.addLink(host4, switch3, 0, 4)
        self.addLink(host5, switch3, 0, 5)
        self.addLink(host6, switch3, 0, 6)
        self.addLink(host7, switch3, 0, 7)
        self.addLink(host8, switch3, 0, 8)
        self.addLink(host9, switch2, 0, 2)

        self.addLink(switch3, switch1, 9, 1)
        self.addLink(switch1, switch2, 2, 1)

        #self.addLink(switch3, switch2, 3, 4)

        #self.addLink(switch2, switch4, 2, 1)
        #self.addLink(host4, switch4, 0, 2)
        #self.addLink(host5, switch4, 0, 3)

        #self.addLink( host1, switch1)
        #self.addLink( switch1, switch2)
        #self.addLink( host2, switch1)
        #self.addLink(host3, switch2)
        #self.addLink(host4, switch2)

        #topos = { 'mytopod': ( lambda: MyTopod() )

def readFile(path, flowNum, ruleNum):
    with open(path) as fp:
        for i in range(0, flowNum+3):
            fline = fp.readline().strip().split()

        fline = fp.readline().strip().split()
        flowInterest = int(fline[0])
        fline = fp.readline().strip().split()
        attackFlow = int(fline[0])

    return {'flowInterest': flowInterest, 'attackFlow': attackFlow}

def simpleTest():
    topo = MyTopod()
    net = Mininet(topo=topo, switch=OVSKernelSwitch, controller=RemoteController)


            #c1 = net.addController('c1', controller=RemoteController, ip="127.0.0.1", port=6633)
    net.start()
    s1 = net.get('s1')
    s2 = net.get('s2')
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')
    h5 = net.get('h5')
    h6 = net.get('h6')
    h7 = net.get('h7')
    h8 = net.get('h8')
            #s1 = net.hosts[9]
    print "success!"
    am = 5
    path = "/home/shengliu/Workspace/sdnsim/data1/8_12para1_.txt"
    rdret = readFile(path, 8, 12)
    attackFlow = rdret['attackFlow']
    flowInterest = rdret['flowInterest']
            #for i in range(0, 10):
            #	CLI(net)
            #	print s1.cmd('ovs-ofctl -O openflow13 dump-flows s1')
    sumA = 0
    sumN = 0

    for ct in range(1, 100):

        for i in range(1, 9):
            h10 = net.get('h%d' % i)
            h10.cmd('python poissonProcess.py %d &' % i)
            #if i == flowInterest:
            #    print ret
            #    print flowInterest


        #CLI(net)

        #result = h1.cmd('python trafficGenerate.py')

        sleep (1.5*am)

        #fname = '/home/shengliu/Workspace/mininet/custom/data/result%d' %flowInterest
        #f = open(fname, 'r')
        #print f.readlines()
        #is_shown = f.readlines()[0]
        #is_shown = is_shown.split(',')
        #is_shown = int(is_shown[0])
        #print type(is_shown)
        #f.close()
        #print s1.cmd('ovs-ofctl -O openflow13 dump-flows s1')
        #print s2.cmd('ovs-ofctl -O openflow13 dump-flows s2')
        ht = net.get('h%d' % flowInterest)
        is_shown = ht.cmd('echo')
        #print is_shown
        is_shown = is_shown.strip().split('\n')
        is_shown = is_shown[1]
        is_shown = int(is_shown)
        #print ret[flowInterest]

        #ha = net.get('h%d' % attackFlow)
        ha = net.get('h%d' % flowInterest)

        #result = ha.cmd('echo') #clean the output of & command
        ha.cmd('echo')
        result = ha.cmd('ping 10.0.1.8 -c1')
        #print result
        result = result.strip().split('\n')
        rtt = result[5].strip().split()
        rtt = rtt[3].split('/')
        #print rtt[0]

        if float(rtt[0]) > 1.0:
            attackResult = 0
        else:
            attackResult = 1

        #print attackResult
        #print is_shown
        if is_shown == attackResult:
            sumN = sumN + 1
            #print "attack succeed"
        #else:
            #print "attack failed"
        sleep (2 * am)
        #print sum
        #print ct


        #naive attacker
        for i in range(1, 9):
            h10 = net.get('h%d' % i)
            h10.cmd('python poissonProcess.py %d &' % i)

        sleep (1.5*am)

        ht = net.get('h%d' % flowInterest)
        is_shown = ht.cmd('echo')
        is_shown = is_shown.strip().split('\n')
        is_shown = is_shown[1]
        is_shown = int(is_shown)

        ha = net.get('h%d' % attackFlow)

        ha.cmd('echo')
        result = ha.cmd('ping 10.0.1.8 -c1')

        result = result.strip().split('\n')
        rtt = result[5].strip().split()
        rtt = rtt[3].split('/')

        if float(rtt[0]) > 1.0:
            attackResult = 0
        else:
            attackResult = 1

        if is_shown == attackResult:
            sumA = sumA + 1

        sleep (2 * am)
        print ct

    #is_shown = 1;
    #if rtt[0] == is_shown:
    #    print ("attack succeed")
    #else:
    #    print ("attack fail")

    #sleep(1.5*20)
    #print result[2]
    #print result[3]
    #print h1.cmd('python fping.py')
    #sleep(1)
    #print h1.cmd('ifconfig')
    #print s1.cmd('ovs-ofctl -O openflow13 dump-flows s1')
    #print s2.cmd('ovs-ofctl -O openflow13 dump-flows s2')
            #cmd run in the xterm is actually the behavior of the original desktop
            #print ('h1 completed')
            #h2.cmd('python poissonProcess.py 2 &')
            #print ('h2 completed')
            #h3.cmd('python poissonProcess.py 3 &')
            #print ('h3 completed')
            #h4.cmd('python poissonProcess.py 4 &')
            #print ('h4 completed')
            #h5.cmd('python poissonProcess.py 5 &')
            #h6.cmd('python poissonProcess.py 6 &')
            #h7.cmd('python poissonProcess.py 7 &')
            #h8.cmd('python poissonProcess.py 8 &')
            #print ()

    print sumA
    print sumN
    net.stop()

if __name__ == '__main__':
    simpleTest()
