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
        self.routerTable = StanfordRouterTable().get_route()
        
	#self.rulePriority
	#self.ruleTable = {}
	#self.ruleTable.setdefault(1, ["10.0.0.1", "10.0.0.2", "10.0.0.3"])
	#self.ruleTable.setdefault(2, ["10.0.0.1", "10.0.0.2"])
	#self.ruleTable.setdefault(3, ["10.0.0.1"])
	#for i in range(4,60):
	#	self.ruleTable.setdefault(i, ["10.0.0.%s" %i])
	
	#self.flowRule = {}
	#self.flowRule.setdefault("10.0.0.1", 3)
	#self.flowRule.setdefault("10.0.0.2", 2)
	#self.flowRule.setdefault("10.0.0.3", 1)
	#for i in range(4,60):
	#	self.flowRule.setdefault("10.0.0.%s" %i, i)
	
	self.ruleTable = {}
	self.ruleTable.setdefault("10.0.0.1", ['10.0.0.1', '255.255.255.253', 3])
	self.ruleTable.setdefault("10.0.0.2", ['10.0.0.2', '255.255.255.255', 3])
	self.ruleTable.setdefault("10.0.0.3", ['10.0.0.1', '255.255.255.253', 3])
	self.ruleTable.setdefault("10.0.0.4", ['10.0.0.4', '255.255.255.255', 3])
	for i in range(5,60):
 		self.ruleTable.setdefault('10.0.0.%s' %i, ['10.0.0.%s'%i, '255.255.255.255', 2])
		

	#self.rulePriority = {}
	#self.rulePriority.setdefault(1, 3)
	#self.rulePriority.setdefault(2, 3)
	#self.rulePriority.setdefault(3, 4)
	#for i in range(2,58):
 	#	self.rulePriority.setdefault(i, 2)

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
        
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_FLOOD)]
        self.add_flow(datapath, 0, 0, 0, match, actions)

        
            
        

    def add_flow(self, datapath, idle_timeout, hard_timeout, priority, match, actions):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                             actions)]

        mod = parser.OFPFlowMod(datapath=datapath, idle_timeout=idle_timeout,
                                hard_timeout=hard_timeout, priority=priority,
                                match=match, instructions=inst)
        datapath.send_msg(mod)

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
            



            data = None
            if msg.buffer_id == ofproto.OFP_NO_BUFFER:
                data = msg.data
	    
	    #rule = self.flowRule[dst]
	    #for j in self.ruleTable[rule]:
		#print j

	    match = parser.OFPMatch(eth_type=0x0800, ip_proto=1, ipv4_dst=(self.ruleTable[dst][0],self.ruleTable[dst][1]))
	    out_port = self.routerTable[dpid][dst]
            actions = [parser.OFPActionOutput(out_port)]
	    self.add_flow(datapath, 20, 0, self.ruleTable[dst][2], match, actions)
            
	    out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                      in_port=in_port,  actions=actions, data=data)
            datapath.send_msg(out)
      


class StanfordRouterTable: 

	def __init__(self):
		self.route = {}
		for i in range(1, 17):
			self.route.setdefault(i, {})
		for i in range(1, 5):
			s = ("10.0.0.%s" %i)
			self.route[1][s] = 1
			self.route[2][s] = 17
			self.route[3][s] = 15

		for i in range(5, 30):
			s = ("10.0.0.%s" %i)
			self.route[1][s] = i
			self.route[2][s] = 17
			self.route[3][s] = 15
			

		for i in range(30, 46):
			s = ("10.0.0.%s" %i)
			self.route[1][s] = 30
			self.route[2][s] = i-29
			self.route[3][s] = 16
			
		for i in range(46, 60):
			s = ("10.0.0.%s" %i)
			self.route[1][s] = 31
			self.route[2][s] = 18
			self.route[3][s] = i-45
			
	

	def get_route(self):
		return self.route  
