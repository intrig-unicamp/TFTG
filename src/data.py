from src.generate import *


class generator:
    
    def __init__(self, name):
        #generator
        self.name = name
        self.generation_port = 68
        self.output_port = 0
        self.channel = 0
        self.port_bw = ''
        #TSN
        self.pktlen = 64
        #flags
        self.IP_defined = False
        self.ETH_defined = False
        
    def addGenerationPort(self, port):
        self.generation_port = port
        print(f"==========\nGeneration port:\n{port}")
    
    def addOutputPort(self, port, channel, bw):
        self.output_port = port
        self.channel = channel
        self.port_bw = bw
        print(f"==========\nOutput:\nPhyisical Port: {port}, Port ID: {channel}, bandwitch: {bw}")
        
    def addFlow(self, name, mode="computed", pcp=7, pktlen=654, eth_dst="00:01:02:03:04:05", eth_src="00:06:07:08:09:0a", ip_src="198.168.1.0", ip_dst="198.168.1.1"):
        self.name = name
        self.mode = mode
        self.vlan_pcp = pcp
        self.pktlen = pktlen
        self.eth_dst = eth_dst
        self.eth_src = eth_src
        self.ip_src = ip_src
        self.ip_dst = ip_dst
        
    def histogram(self, name, file):
        self.name = name
        self.file = file

    def distribuition(self, name, sendInt=10000, intStdDev =10):
        self.name = name
        self.sendInt = sendInt
        self.intStdDev = intStdDev
    
    def setGateControl (self, mode):
        self.mode = mode
        
    def setGclPriPort(self, channel, pcp, timeOpen, timeClosed, offset):
        self.channel = channel
        self.vlan_pcp = pcp
        self.timeOpen = timeOpen
        self.timeClosed = timeClosed
        self.offset = offset
        
    def setGB(self, flag):
        self.flag = flag
    
    def setSyncPort(self, port, channel):
        self.output_port = port #seria a mesma porta de output ou seria outro parametro?
        self.channel = channel
        
    def addEthernet(self, eth_src = None, eth_dst = None, type = 'Ipv4',data = None):
        self.ETH_defined = True
        self.eth_dst = eth_dst
        self.eth_src = eth_src
        self.type = type
        self.data = data
       
    def addIP(self, pktlen=64,ip_src="192.168.0.1", ip_dst="192.168.0.2", ip_tos=0, ip_ttl=64, ip_id=0x0001, ip_proto=0):
        self.IP_defined = True
        self.pktlen = pktlen
        self.ip_src = ip_src
        self.ip_dst = ip_dst
        self.ip_tos = ip_tos
        self.ip_ttl = ip_ttl
        self.ip_id = ip_id
        self.ip_proto = ip_proto
        
    #send to generateFiles
    def generate(self):
        
        generatePortConfig(self.output_port, self.channel, self.port_bw) # type: ignore
        generateP4() # type: ignore
        generateControlPlane() # type: ignore
        generateTGentries() # type: ignore