routeing_protocols = ['RIP', 'IGRP', 'EIGRP', 'OSPF', 'ISIS', 'BGP']
link_state_protocols = ['OSPF', 'ISIS']
for protocols in routeing_protocols:
    if protocols not in link_state_protocols:
        print(protocols + '不属于链路状态路由协议。')
