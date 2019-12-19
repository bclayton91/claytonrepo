vrf = "ME11"
routetarget = "4769:5754002"                                  ##Route-target import on the configured router
loopbk = "loopback911"                                        ##Sham-link loopback interface
source = "FC00:10:125:94::21"                                 ##Loopback ipv6 address
destination = "FC00:10:125:94::21"                            ##Loopback ipv6 address on destination router
network = (source) + "/128"                                  
cost = "10"                                                   
procid = "1111"                                               ##Ospfv3 process id



print ("vrf definition", (vrf))
print ("route-target import", (routetarget))
print ("                                ")
print ("interface", (loopbk))
print ("no shutdown")
print ("                                ")
print ("router bgp 4769")
print ("address-family ipv6 vrf", (vrf))
print ("network", (network))
print ("                                ")
print ("router ospfv3", (procid))
print ("address-family ipv4 unicast vrf", (vrf))
print ("area 0 sham-link", (source), (destination), "cost", (cost))