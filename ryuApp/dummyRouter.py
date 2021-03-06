from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.lib.packet import ipv4

class SimpleRouter(app_manager.RyuApp):

    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):

        super(SimpleRouter, self).__init__(*args, **kwargs)

        path = "/home/shengliu/Workspace/mininet/custom/controllerConfig.txt"

        self.routerTable={}
        self.routerTable.setdefault(1, {})
        self.routerTable.setdefault(2, {})
        self.routerTable[1]["10.0.1.0"] = 1
        self.routerTable[1]["10.0.1.1"] = 1
        self.routerTable[1]["10.0.1.2"] = 1
        self.routerTable[1]["10.0.1.3"] = 1
        self.routerTable[1]["10.0.1.4"] = 1
        self.routerTable[1]["10.0.1.5"] = 1
        self.routerTable[1]["10.0.1.6"] = 1
        self.routerTable[1]["10.0.1.7"] = 1
        self.routerTable[1]["10.0.1.8"] = 2

        self.routerTable[2]["10.0.1.0"] = 1
        self.routerTable[2]["10.0.1.1"] = 1
        self.routerTable[2]["10.0.1.2"] = 1
        self.routerTable[2]["10.0.1.3"] = 1
        self.routerTable[2]["10.0.1.4"] = 1
        self.routerTable[2]["10.0.1.5"] = 1
        self.routerTable[2]["10.0.1.6"] = 1
        self.routerTable[2]["10.0.1.7"] = 1
        self.routerTable[2]["10.0.1.8"] = 2


        result = self.readFile(path, 8, 12)
        self.ruleTable = result['ruleTable']
        self.flowPara = result['flowPara']
        self.flowRuleTable = result['flowRuleTable']
        self.flowInterest = result['flowInterest']
        self.attackFlow = result['attackFlow']

#	self.ruleTable[1] = ['10.0.0.3','255.255.255.255', 3, TTL]
#	self.flowRuleTable[flow] = rule

    def readFile(self, path, flowNum, ruleNum):
        fac = 10
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


            flowRuleTable = {} #flowRuleTable[flow] = rule
            for i in range(0, flowNum):
                hs = '10.0.1.%d' %i
                flowRuleTable[hs] = 0
                rp = 0
                for j in range(0, ruleNum):
                    if flowRule[i][j] > rp:
                        flowRuleTable[hs] = j
                        rp = flowRule[i][j]
                flowRuleTable[hs] = flowRuleTable[hs] + 1

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
            ruleSrc = self.getRule()
            for i in range(0, ruleNum):
                ruleTable[i+1] = [ruleSrc[ruleRd[i]][0], ruleSrc[ruleRd[i]][1], rPrt[i] + 1, fac * TTL[i]]

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

        return NULL;



    def getRule(self):
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

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
       # print(datapath.id)
        dpid = datapath.id
        if dpid < 100:

            match = parser.OFPMatch(eth_type=0x0800, ip_proto=1)
            actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                          ofproto.OFPCML_NO_BUFFER)]
            self.add_flow(datapath, 0, 0, 1, match, actions)

            match = parser.OFPMatch(eth_type=0x0800, ip_proto=1, ipv4_src='10.0.1.8')
            out_port = 1
            actions = [parser.OFPActionOutput(out_port)]
            self.add_flow(datapath, 0, 0, 2, match, actions)

        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_FLOOD)]
        self.add_flow(datapath, 0, 0, 0, match, actions)





    def add_flow(self, datapath, idle_timeout, hard_timeout, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]

        print idle_timeout
        mod = parser.OFPFlowMod(datapath=datapath, idle_timeout=idle_timeout,
                                hard_timeout=hard_timeout, priority=priority,
                                match=match, instructions=inst)
        datapath.send_msg(mod)
        print ("add rule!")

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def _packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        dpid = datapath.id
        in_port = msg.match['in_port']

        pkt = packet.Packet(msg.data)
        pkt_ipv4 = pkt.get_protocols(ipv4.ipv4)
        if len(pkt_ipv4) > 0:
            pkt_ipv4 = pkt_ipv4[0]
            dst = pkt_ipv4.dst
            src = pkt_ipv4.src
	    print dst
	    print src

	    out_port = self.routerTable[dpid][dst]
	    rule = self.flowRuleTable[src]
	    prt = self.ruleTable[rule][2]
	    TTL = self.ruleTable[rule][3]
	    print rule
        match = parser.OFPMatch(eth_type=0x0800, ip_proto=1, ipv4_src=(self.ruleTable[rule][0], self.ruleTable[rule][1]), ipv4_dst=(dst, '255.255.255.255'))
        actions = [parser.OFPActionOutput(out_port)]

        #print TTL
        self.add_flow(datapath, TTL, 0, prt, match, actions)

        data = None
        if msg.buffer_id == ofproto.OFP_NO_BUFFER:
            data = msg.data
       #    print ("data included")

        out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id, in_port=in_port,  actions=actions, data=data)
        datapath.send_msg(out)
        #print("msg sent")


        #out_port = self.routerTable[dpid][src]
        #match = parser.OFPMatch(eth_type=0x0800, ip_proto=1, ipv4_src=(dst, '255.255.255.255'), ipv4_dst=(self.ruleTable[rule][0], self.ruleTable[rule][1]))
        #actions = [parser.OFPActionOutput(out_port)]

        #self.add_flow(datapath, TTL, 0, prt, match, actions)
