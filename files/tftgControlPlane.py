#from netaddr import IPAddress
p4 = bfrt.tftg.pipe

fwd_table = p4.SwitchIngress.fwd
time_table = p4.SwitchIngress.time


time_table.add(delay=263)
time_table.add(delay=312)
time_table.add(delay=304)
time_table.add(delay=130)


fwd_table.add_with_send(ctrl=2, port=160)

bfrt.complete_operations()