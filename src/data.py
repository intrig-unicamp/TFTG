from src.generate import *


class Flow:
    def __init__(self, name, outputPort=None, fixedDelay=None, histogramDelay=None, pcp=0, pktlen=1000, eth_dst="00:01:02:03:04:05", eth_src="00:06:07:08:09:0a", ip_src="192.168.1.1", ip_dst="192.168.1.2", delayMode=None):
        self.name = name
        self.fixedDelay = fixedDelay
        self.histogramDelay = histogramDelay
        self.vlan_pcp = pcp
        self.eth_dst = eth_dst
        self.eth_src = eth_src
        self.ip_src = ip_src
        self.ip_dst = ip_dst
        self.pktlen = pktlen
        self.pcp = pcp

        self.outputPort = outputPort
        
        #flags
        self.delayMode = delayMode


class Port:
    def __init__(self, port, channel, bw):
        self.port = port
        self.channel = channel
        self.bw = bw
        


class generator:

    def __init__(self, name):
        #generator
        self.name = name
        self.generation_port = 68

        self.physicalPorts = []
        

        self.flowsFixed = []
        self.flowsHistogram = []

        #TSN
        self.pktlen = 64
        self.fixedDelay = 10000
        self.histogramDelay = 'NULL'
        self.vlan_pcp = 0
        self.eth_dst = "00:01:02:03:04:05"
        self.eth_src = "00:06:07:08:09:0a"
        self.ip_src = "192.168.1.1"
        self.ip_dst = "192.168.1.2"
        
        #flags
        self.IP_defined = False
        self.ETH_defined = False
        self.delayMode = ''
        
    def addGenerationPort(self, port):
        self.generation_port = port
        
    
    def addOutputPort(self, port, channel, bw):

        self.physicalPorts.append(Port(port, channel, bw))

        
        
    def addFlow(self, name, outputPort=None, fixedDelay=None, histogramDelay=None,pcp=0, pktlen=1000, eth_dst="00:01:02:03:04:05", eth_src="00:06:07:08:09:0a", ip_src="192.168.1.1", ip_dst="192.168.1.2"):
        
        if outputPort is None:
            raise ValueError("Output port must be defined.")

        # Verifica qual delay foi definido
        if fixedDelay is not None and histogramDelay is not None:
            raise ValueError("You should define type of delay: 'fixedDelay' or 'histogramDelay', never both.")
        elif fixedDelay is not None:
            flow = Flow(name, outputPort, fixedDelay, histogramDelay, pcp, pktlen, eth_dst, eth_src, ip_src, ip_dst, delayMode="fixed")
            self.flowsFixed.append(flow)
        elif histogramDelay is not None:
            flow = Flow(name, outputPort, fixedDelay, histogramDelay, pcp, pktlen, eth_dst, eth_src, ip_src, ip_dst, delayMode="histogram")
            self.flowsHistogram.append(flow)
        else:
            raise ValueError("You must define at least one delay: 'fixedDelay' or 'histogramDelay'.")
        


    def histogram(self, name, file, delayMode=1):
        self.name = name
        self.file = file
        self.delayMode = delayMode

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
        

    def printInfo(self):
        print("==========\nGenerator Info:")
        print(f"==========\nGeneration port:\n{self.generation_port}")
        print("==========\nPhysical Ports:")
        for port in self.physicalPorts:
            print(f"Physical Port: {port.port}, Port ID: {port.channel}, Bandwidth: {port.bw}")

        print("==========\nFlows:")
        for flow in self.flowsFixed:
            bits_per_packet = flow.pktlen * 8
            seconds_per_packet = flow.fixedDelay / 1e9
            packets_per_second = 1 / seconds_per_packet
            throughput_bps = bits_per_packet * packets_per_second
            throughput_mbps = throughput_bps / 1e6
            print(f"Flow: {flow.name}, Output Port: {flow.outputPort}, Fixed Delay: {flow.fixedDelay}, Packet Size: {flow.pktlen}, Expected Throughput: {throughput_mbps:.2f} Mbps")
        for flow in self.flowsHistogram:
            print(f"Flow: {flow.name}, Output Port: {flow.outputPort}, Fixed Delay: {flow.fixedDelay}, Histogram Delay: {flow.histogramDelay}, PCF: {flow.vlan_pcp}, Eth_dst: {flow.eth_dst}, Eth_src: {flow.eth_src}, IP_src: {flow.ip_src}, IP_dst: {flow.ip_dst}")
        print("==========\n")        

    #send to generateFiles
    def generate(self):
        
        self.printInfo()

        generatePortConfig(self.physicalPorts) # type: ignore
        generateP4() # type: ignore
        generateControlPlane(self.flowsHistogram, self.flowsFixed) # type: ignore


        generateTGentries(self.generation_port, self.flowsFixed, self.flowsHistogram) # type: ignore