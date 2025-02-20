import re
import random

def generateTGentries(generation_port):
    entries = open("files/TGEntries.py", "w")
    
    
    entries.write('#!/usr/bin/env python\n')
    entries.write('import sys\n')
    entries.write('import os\n')
    entries.write('import time\n')
    entries.write("sys.path.append(os.path.expandvars('$SDE/install/lib/python3.6/site-packages/tofino/'))\n")
    entries.write("sys.path.append(os.path.expandvars('$SDE/install/lib/python3.6/site-packages/'))\n")
    entries.write("sys.path.append(os.path.expandvars('$SDE/install/lib/python3.6/site-packages/bf_ptf/'))\n")
    entries.write('import grpc\n')
    entries.write('import bfrt_grpc.bfruntime_pb2 as bfruntime_pb2\n')
    entries.write('import bfrt_grpc.client as gc\n\n')

    entries.write('import ptf.testutils as testutils\n\n')

    entries.write('# Connect to BF Runtime Server\n')
    entries.write('interface = gc.ClientInterface(grpc_addr = "localhost:50052",\n')
    entries.write('                            client_id = 0,\n')
    entries.write('                            device_id = 0)\n')
    entries.write("print('Connected to BF Runtime Server')\n\n")

    entries.write('# Get the information about the running program on the bfrt server.\n')
    entries.write('bfrt_info = interface.bfrt_info_get()\n')
    entries.write("print('The target runs program ', bfrt_info.p4_name_get())\n\n")

    entries.write('# Establish that you are working with this program\n')
    entries.write('interface.bind_pipeline_config(bfrt_info.p4_name_get())\n\n')

    entries.write('####### You can now use BFRT CLIENT #######\n')
    entries.write('target = gc.Target(device_id=0, pipe_id=0xffff)\n\n\n')



    entries.write('print("configure timer table")\n')
    #entries.write('i_port = 68     # Default port for pktgen\n')
    entries.write('pipe_id = 0\n')
    entries.write('g_timer_app_id = 1\n')
    entries.write('batch_id = [0,1,2,3] # 0,1,2,3\n')
    entries.write('packet_id = [0,1] # 0,1\n')
    entries.write('#o_port = 160     # HW port to send the packets\n\n')



    entries.write('pktgen_app_cfg_table = bfrt_info.table_get("app_cfg")\n')
    entries.write('pktgen_pkt_buffer_table = bfrt_info.table_get("pkt_buffer")\n')
    entries.write('pktgen_port_cfg_table = bfrt_info.table_get("port_cfg")\n\n')

    entries.write('app_id = g_timer_app_id\n')
    entries.write('pktlen = 1024\n')
    entries.write('pgen_pipe_id = 0\n')
    entries.write(f'src_port = {generation_port}\n')
    entries.write('p_count = 1  # packets per batch\n')
    entries.write('b_count = 1  # batch number\n')
    entries.write('buff_offset = 144  # generated packets payload will be taken from the offset in buffer\n\n')

    entries.write('# build expected generated packets\n')
    entries.write('print("Create packet")\n')
    entries.write('p = testutils.simple_ipv4ip_packet(pktlen=pktlen)\n\n')

    entries.write('print("enable pktgen port")\n\n')

    entries.write('pktgen_port_cfg_table.entry_mod(\n')
    entries.write('target,\n')
    entries.write("[pktgen_port_cfg_table.make_key([gc.KeyTuple('dev_port', src_port)])],\n")
    entries.write("[pktgen_port_cfg_table.make_data([gc.DataTuple('pktgen_enable', bool_val=True)])])\n\n")

    entries.write('# Configure the packet generation timer application\n')
    entries.write('print("configure pktgen application")\n')
    entries.write("data = pktgen_app_cfg_table.make_data([gc.DataTuple('timer_nanosec', 1),\n")
    entries.write("                                gc.DataTuple('app_enable', bool_val=False),\n")
    entries.write("                                gc.DataTuple('pkt_len', (pktlen - 6)),\n")
    entries.write("                                gc.DataTuple('pkt_buffer_offset', buff_offset),\n")
    entries.write("                                gc.DataTuple('pipe_local_source_port', src_port),\n")
    entries.write("                                gc.DataTuple('increment_source_port', bool_val=False),\n")
    entries.write("                                gc.DataTuple('batch_count_cfg', b_count - 1),\n")
    entries.write("                                gc.DataTuple('packets_per_batch_cfg', p_count - 1),\n")
    entries.write("                                gc.DataTuple('ibg', 0),\n")
    entries.write("                                gc.DataTuple('ibg_jitter', 0),\n")
    entries.write("                                gc.DataTuple('ipg', 0),\n")
    entries.write("                                gc.DataTuple('ipg_jitter', 0),\n")
    entries.write("                                gc.DataTuple('batch_counter', 0),\n")
    entries.write("                                gc.DataTuple('pkt_counter', 0),\n")
    entries.write("                                gc.DataTuple('trigger_counter', 0)],\n")
    entries.write("                                'trigger_timer_periodic')\n")
    entries.write('pktgen_app_cfg_table.entry_mod(\n')
    entries.write('target,\n')
    entries.write("[pktgen_app_cfg_table.make_key([gc.KeyTuple('app_id', g_timer_app_id)])],\n")
    entries.write('[data])\n\n')


    entries.write('print("configure packet buffer")\n')
    entries.write('pktgen_pkt_buffer_table.entry_mod(\n')
    entries.write('target,\n')
    entries.write("[pktgen_pkt_buffer_table.make_key([gc.KeyTuple('pkt_buffer_offset', buff_offset),\n")
    entries.write("                                gc.KeyTuple('pkt_buffer_size', (pktlen - 6))])],\n")
    entries.write("[pktgen_pkt_buffer_table.make_data([gc.DataTuple('buffer', bytearray(bytes(p)[6:]))])])  # p[6:]))])\n\n")


    entries.write('print("enable pktgen")\n')
    entries.write('pktgen_app_cfg_table.entry_mod(\n')
    entries.write('target,\n')
    entries.write("[pktgen_app_cfg_table.make_key([gc.KeyTuple('app_id', g_timer_app_id)])],\n")
    entries.write("[pktgen_app_cfg_table.make_data([gc.DataTuple('app_enable', bool_val=True)],\n")
    entries.write("                                'trigger_timer_periodic')]\n")
    entries.write(')')
    
    

def generateControlPlane(channel, file, delayMode):
    control = open("files/tftgControlPlane.py", "w")
    histogram = open(f"files/{file}", "r")
    content = histogram.read()
    histogram.close()
    
    delays = []
    packets = []
    
    control.write('#from netaddr import IPAddress\n')
    control.write('p4 = bfrt.tftg.pipe\n\n')

    control.write('fwd_table = p4.SwitchIngress.fwd\n')
    control.write('time_table = p4.SwitchIngress.time\n\n\n')
    
    macthes = re.findall(r'<bin low="(\d+)ms">(\d+)</bin>', content)
    for delay, packet in macthes:
        delays.append(int(delay))
        packets.append(int(packet))
        
    if delayMode == 2:
        random.shuffle(delays)
        
    elif delayMode == 3:
        new_delays = []
        for i in range(len(delays)):
            if i < len(delays) - 1 and delays[i] + 1 < delays[i + 1]:
                new_delays.append(random.randint(delays[i] + 1, delays[i + 1] - 1))
            elif i == len(delays) - 1 and len(delays) > 1:
                lower_bound = delays[i - 1] + 1
                upper_bound = delays[i] - 1
                if lower_bound <= upper_bound:
                    new_delays.append(random.randint(lower_bound, upper_bound))
        delays = new_delays
        random.shuffle(delays)
        
    for delay in delays:
        control.write(f'time_table.add(delay={delay})\n')
    
    control.write('\n\n')
    control.write(f'fwd_table.add_with_send(ctrl=2, port={channel})\n\n')

    control.write('bfrt.complete_operations()')
    control.close()
    
def generatePortConfig(output_port, channel, port_bw):
    ports = open("files/portConfig", "w")
    
    ports.write('ucli\n')
    ports.write('pm\n')
    ports.write(f'port-add {output_port}/- {port_bw} NONE\n')
    ports.write(f'port-enb {output_port}/-\n')
    ports.write(f'an-set {output_port}/- 2 \n')
    ports.write(f'port-dis {output_port}/-\n')
    ports.write(f'port-enb {output_port}/-\n')
    ports.write('show\n')
    ports.write('exit\n')
    ports.write('exit\n')
    
    
def generateP4():

    filep4 = open("files/tftg.p4", "w")
    
    filep4.write('#include <tna.p4>\n\n')

    filep4.write('typedef bit<48> mac_addr_t;\n')
    filep4.write('typedef bit<12> vlan_id_t;\n')
    filep4.write('typedef bit<16> ether_type_t;\n')
    filep4.write('typedef bit<32> ipv4_addr_t;\n\n')

    filep4.write('const ether_type_t ETHERTYPE_IPV4 = 16w0x0800;\n')
    filep4.write('const ether_type_t ETHERTYPE_VLAN = 16w0x8100;\n\n')



    filep4.write('header ethernet_h {\n')
    filep4.write('    mac_addr_t dst_addr;\n')
    filep4.write('    mac_addr_t src_addr;\n')
    filep4.write('    bit<16> ether_type;\n')
    filep4.write('}\n\n')

    filep4.write('header vlan_tag_h {\n')
    filep4.write('    bit<3> pcp;\n')
    filep4.write('    bit<1> cfi;\n')
    filep4.write('    vlan_id_t vid;\n')
    filep4.write('    bit<16> ether_type;\n')
    filep4.write('}\n\n')

    filep4.write('header ipv4_h {\n')
    filep4.write('    bit<4> version;\n')
    filep4.write('    bit<4> ihl;\n')
    filep4.write('    bit<8> diffserv;\n')
    filep4.write('    bit<16> total_len;\n')
    filep4.write('    bit<16> identification;\n')
    filep4.write('    bit<16> flags;\n')
    filep4.write('    bit<8> ttl;\n')
    filep4.write('    bit<8> protocol;\n')
    filep4.write('    bit<16> hdr_checksum;\n')
    filep4.write('    ipv4_addr_t src_addr;\n')
    filep4.write('    ipv4_addr_t dst_addr;\n')
    filep4.write('}\n\n')

    filep4.write('struct headers {\n')
    filep4.write('    pktgen_timer_header_t timer;\n')
    filep4.write('    ethernet_h	ethernet;\n')
    filep4.write('    vlan_tag_h	vlan_tag;\n')
    filep4.write('    ipv4_h		ipv4;\n')
    filep4.write('}\n\n')

    filep4.write('struct my_ingress_metadata_t {\n')
    filep4.write('    bit<8> ctrl;\n')
    filep4.write('}\n\n')

    filep4.write('struct my_egress_metadata_t {\n')
    filep4.write('\n')
    filep4.write('}\n\n')

    filep4.write('parser SwitchIngressParser(\n')
    filep4.write('    packet_in packet, \n')
    filep4.write('    out headers hdr, \n')
    filep4.write('    out my_ingress_metadata_t ig_md,\n')
    filep4.write('    out ingress_intrinsic_metadata_t ig_intr_md) {\n\n')

    filep4.write('    state start {\n')
    filep4.write('        packet.extract(ig_intr_md);\n')
    filep4.write('        packet.advance(PORT_METADATA_SIZE);\n\n')
            
    filep4.write('        pktgen_timer_header_t pktgen_pd_hdr = packet.lookahead<pktgen_timer_header_t>();\n')
    filep4.write('        transition select(pktgen_pd_hdr.app_id) {\n')
    filep4.write('            1 : parse_pktgen_timer;\n')
    filep4.write('            default : reject;\n')
    filep4.write('        }\n')
    filep4.write('    }\n\n')

    filep4.write('    state parse_pktgen_timer {\n')
    filep4.write('        //packet.extract(hdr.timer);\n')
    filep4.write('        ig_md.ctrl = 2;\n')
    filep4.write('        transition parse_ethernet;\n')
    filep4.write('    }\n\n')

    filep4.write('    state parse_ethernet {\n')
    filep4.write('        packet.extract(hdr.ethernet);\n')
    filep4.write('        transition select(hdr.ethernet.ether_type) {\n')
    filep4.write('            ETHERTYPE_IPV4:  parse_ipv4;\n')
    filep4.write('            ETHERTYPE_VLAN:  parse_vlan;\n')
    filep4.write('            default: accept;\n')
    filep4.write('        }\n')
    filep4.write('    }\n\n')

    filep4.write('    state parse_vlan {\n')
    filep4.write('        packet.extract(hdr.vlan_tag);\n')
    filep4.write('        transition select(hdr.vlan_tag.ether_type) {\n')
    filep4.write('            ETHERTYPE_IPV4:  parse_ipv4;\n')
    filep4.write('            default: accept;\n')
    filep4.write('        }\n')
    filep4.write('    }\n\n')
        
    filep4.write('    state parse_ipv4 {\n')
    filep4.write('        packet.extract(hdr.ipv4);\n')
    filep4.write('        transition accept;\n')
    filep4.write('    }\n')
    filep4.write('}\n\n')


    filep4.write('control SwitchIngress(\n')
    filep4.write('    inout headers hdr, \n')
    filep4.write('    inout my_ingress_metadata_t ig_md,\n')
    filep4.write('    in ingress_intrinsic_metadata_t ig_intr_md,\n')
    filep4.write('    in ingress_intrinsic_metadata_from_parser_t ig_intr_prsr_md,\n')
    filep4.write('    inout ingress_intrinsic_metadata_for_deparser_t ig_intr_dprsr_md,\n')
    filep4.write('    inout ingress_intrinsic_metadata_for_tm_t ig_intr_tm_md) {\n\n')
            
    filep4.write('    action drop() {\n')
    filep4.write('        ig_intr_dprsr_md.drop_ctl = 0x1;\n')
    filep4.write('    }\n\n')
        
    filep4.write('    action send(PortId_t port) {\n')
    filep4.write('        ig_intr_tm_md.ucast_egress_port = port;\n')
    filep4.write('    }\n\n')
    
    filep4.write('    table fwd {\n')
    filep4.write('        key = {\n')
    filep4.write('            ig_md.ctrl	:	exact;\n')
    filep4.write('        }\n')
    filep4.write('        actions = {\n')
    filep4.write('            send;\n')
    filep4.write('            drop;\n')
    filep4.write('        }\n')
    filep4.write('        const default_action = drop();\n')
    filep4.write('        size = 1024;\n')
    filep4.write('    }\n\n')
            
    filep4.write('    apply {\n\n')
            
    filep4.write('        fwd.apply();\n\n')
            
    filep4.write('    }\n\n')
            
    filep4.write('}\n\n')


    filep4.write('control SwitchIngressDeparser(\n')
    filep4.write('    packet_out pkt,\n')
    filep4.write('    inout headers hdr,\n')
    filep4.write('    in my_ingress_metadata_t ig_md,\n')
    filep4.write('    in ingress_intrinsic_metadata_for_deparser_t ig_intr_dprsr_md) {\n\n')

    filep4.write('    apply {\n')
    filep4.write('        pkt.emit(hdr);\n')
    filep4.write('    }\n')
    filep4.write('}\n\n')


    filep4.write('parser SwitchEgressParser(\n')
    filep4.write('    packet_in packet,\n')
    filep4.write('    out headers hdr,\n')
    filep4.write('    out my_egress_metadata_t eg_md,\n')
    filep4.write('    out egress_intrinsic_metadata_t eg_intr_md) {\n\n')
        
    filep4.write('    state start {\n')
    filep4.write('        packet.extract(eg_intr_md);\n')
    filep4.write('        transition parse_ethernet;\n')
    filep4.write('    }\n\n')
        
    filep4.write('    state parse_ethernet {\n')
    filep4.write('        packet.extract(hdr.ethernet);\n')
    filep4.write('        transition select(hdr.ethernet.ether_type) {\n')
    filep4.write('            ETHERTYPE_IPV4:  parse_ipv4;\n')
    filep4.write('            ETHERTYPE_VLAN:  parse_vlan;\n')
    filep4.write('            default: accept;\n')
    filep4.write('        }\n')
    filep4.write('    }\n\n')

    filep4.write('    state parse_vlan {\n')
    filep4.write('        packet.extract(hdr.vlan_tag);\n')
    filep4.write('        transition select(hdr.vlan_tag.ether_type) {\n')
    filep4.write('            ETHERTYPE_IPV4:  parse_ipv4;\n')
    filep4.write('            default: accept;\n')
    filep4.write('        }\n')
    filep4.write('    }\n\n')
        
    filep4.write('    state parse_ipv4 {\n')
    filep4.write('        packet.extract(hdr.ipv4);\n')
    filep4.write('        transition accept;\n')
    filep4.write('    }\n')
    filep4.write('}\n\n')


    filep4.write('control SwitchEgress(\n')
    filep4.write('    inout headers hdr,\n')
    filep4.write('    inout my_egress_metadata_t eg_md,\n')
    filep4.write('    in egress_intrinsic_metadata_t eg_intr_md,\n')
    filep4.write('    in egress_intrinsic_metadata_from_parser_t eg_intr_md_from_prsr,\n')
    filep4.write('    inout egress_intrinsic_metadata_for_deparser_t ig_intr_dprs_md,\n')
    filep4.write('    inout egress_intrinsic_metadata_for_output_port_t eg_intr_oport_md) {\n\n')
            
    filep4.write('    apply {\n\n')
            
    filep4.write('    }\n')
    filep4.write('}\n\n')

    filep4.write('control SwitchEgressDeparser(\n')
    filep4.write('    packet_out pkt,\n')
    filep4.write('    inout headers hdr,\n')
    filep4.write('    in my_egress_metadata_t eg_md,\n')
    filep4.write('    in egress_intrinsic_metadata_for_deparser_t ig_intr_dprs_md) {\n')
            
    filep4.write('    apply {\n')
    filep4.write('        pkt.emit(hdr);\n')
    filep4.write('    }\n')
    filep4.write('}\n\n')

    filep4.write('Pipeline(SwitchIngressParser(),\n')
    filep4.write('        SwitchIngress(),\n')
    filep4.write('        SwitchIngressDeparser(),\n')
    filep4.write('        SwitchEgressParser(),\n')
    filep4.write('        SwitchEgress(),\n')
    filep4.write('        SwitchEgressDeparser()) pipe;\n\n')

    filep4.write('Switch(pipe) main;')