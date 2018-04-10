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
        self.routerTable={}
        self.routerTable.setdefault(1, {})
        self.routerTable.setdefault(2, {})
        self.routerTable[1]["10.0.0.1"] = 1;
        self.routerTable[1]["10.0.0.2"] = 2;
        self.routerTable[1]["10.0.0.3"] = 3;
        self.routerTable[1]["10.0.0.4"] = 3;
        self.routerTable[2]["10.0.0.1"] = 3;
        self.routerTable[2]["10.0.0.2"] = 3;
        self.routerTable[2]["10.0.0.3"] = 1;
        self.routerTable[2]["10.0.0.4"] = 2;

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        
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
            out_port = self.routerTable[dpid][dst]

            match = parser.OFPMatch(eth_type=0x0800, ip_proto=1, ipv4_dst=dst)
            actions = [parser.OFPActionOutput(out_port)]

            data = None
            if msg.buffer_id == ofproto.OFP_NO_BUFFER:
                data = msg.data

            self.add_flow(datapath, 20, 0, 2, match, actions)
            out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                      in_port=in_port,  actions=actions, data=data)
            datapath.send_msg(out)
        
