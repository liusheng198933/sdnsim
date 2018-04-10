from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ipv4
from ryu.lib.packet import ether_types
from ryu.lib.packet import icmp


class SimpleSwitch(app_manager.RyuApp):
      OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

      def __init__(self, *args, **kwargs):
            super(SimpleSwitch, self).__init__(*args, **kwargs)
            self.mac_to_port = {}

      @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
      def switch_features_handler(self, ev):
            datapath = ev.msg.datapath
            ofproto = datapath.ofproto
            parser = datapath.ofproto_parser

            match = parser.OFPMatch()
            actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER,
                                              ofproto.OFPCML_NO_BUFFER)]
            self.add_flow(datapath, 0, match, actions)

      def add_flow(self, datapath, priority, match, actions, buffer_id=None):
            ofproto = datapath.ofproto
            parser = datapath.ofproto_parser

            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS,
                                                 actions)]
            if buffer_id:
                  mod = parser.OFPFlowMod(datapath=datapath, buffer_id=buffer_id,
                                           priority=priority, match=match,
                                           instructions=inst)
            else:
                  mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                                          match=match, instructions=inst)
            datapath.send_msg(mod)
            
      #decorator for packet_in handler      
      @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
      def _packet_in_handler(self, ev):
            if ev.msg.msg_len < ev.msg.total_len:
                  self.logger.debug("packet truncated: only %s of %s bytes",
                                    ev.msg.msg_len, ev.msg.total_len)
            
            msg = ev.msg
            datapath = msg.datapath
            ofproto = datapath.ofproto
            parser = datapath.ofproto_parser
            in_port = msg.match['in_port']

            pkt = packet.Packet(msg.data)
            eth = pkt.get_protocols(ethernet.ethernet)[0]
            
            pkt_ipv4 = pkt.get_protocols(ipv4.ipv4)
            if len(pkt_ipv4) > 0:
                  pkt_ipv4 = pkt_ipv4[0]
                  dst = pkt_ipv4.dst
                  src = pkt_ipv4.src
                  print("haha ipv4 packet")
                  print(type(dst))
                  pkt_icmp = pkt.get_protocols(icmp.icmp)
                  print(pkt_icmp)
     

            if eth.ethertype == ether_types.ETH_TYPE_LLDP:
                  return
            dst = eth.dst
            src = eth.src

            dpid = datapath.id
            
            self.mac_to_port.setdefault(dpid, {})

            #self.logger.info("packet in %s %s %s %s", dpid, src, dst, in_port)

            self.mac_to_port[dpid][src] = in_port

            if dst in self.mac_to_port[dpid]:
                  out_port = self.mac_to_port[dpid][dst]
            else:
                  out_port = ofproto.OFPP_FLOOD

            actions = [parser.OFPActionOutput(out_port)]

            #print(dpid)
            #print(type(dpid))
            #print(in_port)
            #print(type(in_port))
            
            if out_port != ofproto.OFPP_FLOOD:
                  match = parser.OFPMatch(in_port=in_port, eth_dst=dst)
                  self.add_flow(datapath, 1, match, actions)

            data = None
            if msg.buffer_id == ofproto.OFP_NO_BUFFER:
                  data = msg.data

            out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                      in_port=in_port, actions=actions, data=data)
            datapath.send_msg(out)
            
            