#from netaddr import IPAddress
p4 = bfrt.tftg.pipe

fwd_table = p4.SwitchIngress.fwd

fwd_table.add_with_send(ctrl=2, port=164)

bfrt.complete_operations()
