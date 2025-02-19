#from netaddr import IPAddress
p4 = bfrt.tftg.pipe

fwd_table = p4.SwitchIngress.fwd
time_table = p4.SwitchIngress.time


time_table.add(delay=1.521751317799821)
time_table.add(delay=2.8235656979705057)
time_table.add(delay=3.0572620281179046)


fwd_table.add_with_send(ctrl=2, port=160)

bfrt.complete_operations()