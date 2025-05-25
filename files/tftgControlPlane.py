#from netaddr import IPAddress
p4 = bfrt.tftg.pipe

fwd_table = p4.SwitchIngress.fwd


fwd_table.add_with_send(ctrl=1, port=134)

fwd_table.add_with_send(ctrl=2, port=134)

bfrt.complete_operations()