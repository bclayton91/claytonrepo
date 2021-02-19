from Template import router

if router["int_type"] == "bdi":
    print (router["int2"])
    print (router["desc"])
    print ("no negotiation auto")
    print ("no mop enabled")
    print ("no mop sysid")
    print (router["SI"], "ethernet")
    print (router["desc2"])
    print ("encapsulation dot1q", router["tag"], "exact")
    print ("rewrite ingress tag pop 1 symmetric")


    print ("                                        ")
    print ("interface", router["int"])
    print (router["desc2"])
    print ("vrf forwarding", router["vrf"])
    print ("ip address", router["IP"])
    print ("no ip redirects")
    print ("no ip proxy-arp")
    print ("ip pim sparse-mode")
    print ("ip verify unicast source reachable-via rx")
    print ("ipv6 enable")
    if router["routing_protocol"]=="ospfv3":
        print ("ospfv3", router["procID"], "network point-to-point")
        print ("ospfv3", router["procID"], "flood-reduction")
        print ("ospfv3", router["procID"], "ipv4 area 0")


    print ("                                         ")
    print ("bridge-domain", router["bridgedomain"])
    print ("member", router["int2"], router["SI"])
else:
    print ("interface", router["int"])
    print (router["desc2"])
    print ("vrf forwarding", router["vrf"])
    print ("ip address", router["IP"])
    print ("no ip redirects")
    print ("no ip proxy-arp")
    print ("ip pim sparse-mode")
    print ("ip verify unicast source reachable-via rx")
    print ("ipv6 enable")
    if router["routing_protocol"]=="ospfv3":
        print ("ospfv3", router["procID"], "network point-to-point")
        print ("ospfv3", router["procID"], "flood-reduction")
        print ("ospfv3", router["procID"], "ipv4 area 0")


if router["routing_protocol"]=="ospfv3":
    print ("                                         ")
    print ("router ospfv3", router["procID"])
    print ("address-family ipv4 vrf", router["vrf"])
    print ("redistribute bgp 4769")


    print ("                                         ")
    print ("router bgp 4769")
    print ("address-family ipv4 vrf", router["vrf"])
    print ("redistribute connected")
    print ("redistribute ospfv3", router["procID"])

if router["routing_protocol"]=="bgp":
    print ("                                         ")
    print ("address-family ipv4 unicast vrf", router["vrf"])
    print ("neighbor", router["neighbor_ip"], "remote-as", router["remote_as"])
    print ("neighbor", router["neighbor_ip"],router["neighbor_desc"])
    print ("neighbor",router["neighbor_ip"], "ttl-security hops 1")
    print ("neighbor", router["neighbor_ip"], "activate")

