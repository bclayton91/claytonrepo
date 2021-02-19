int = "bdi 430"
int2 = "interface ethernet-internal 1/0/0"       #Only used with BDI interfaces
desc = "description TO SWITCH G0/18"          
SI = "service instance 430"                      #service instance ID
tag = "430"                                      #vlan
desc2 = "description 2BCT local connection"      #description under interfaces
procID = "30"                                    #ospfv3 process ID
vrf = "2BCT"                                     #vrf instance used
bridgedomain = "430"                             #Bridge domain ID
IP = "10.108.64.88 255.255.255.254"              #Ip address of the interface
int_type = "bdi"                                 #For bdi interfaces, use "bdi"
 
if int_type == "bdi":
    print (int2)	
    print (desc)
    print ("no negotiation auto")
    print ("no mop enabled")
    print ("no mop sysid")
    print ((SI), "ethernet")
    print (desc2)
    print ("encapsulation dot1q", (tag), "exact")
    print ("rewrite ingress tag pop 1 symmetric")


    print ("                                        ")
    print ("interface", (int))
    print (desc2)
    print ("vrf forwarding", (vrf))
    print ("ip address", (IP))
    print ("no ip redirects")
    print ("no ip proxy-arp")
    print ("ip pim sparse-mode")
    print ("ip verify unicast source reachable-via rx")
    print ("ipv6 enable")
    print ("ospfv3", (procID), "network point-to-point")
    print ("ospfv3", (procID), "flood-reduction")
    print ("ospfv3", (procID), "ipv4 area 0")


    print ("                                         ")
    print ("bridge-domain", (bridgedomain))
    print ("member", (int2), (SI))
else:
    print ("interface", (int))
    print (desc2)
    print ("vrf forwarding", (vrf))
    print ("ip address", (IP))
    print ("no ip redirects")
    print ("no ip proxy-arp")
    print ("ip pim sparse-mode")
    print ("ip verify unicast source reachable-via rx")
    print ("ipv6 enable")
    print ("ospfv3", (procID), "network point-to-point")
    print ("ospfv3", (procID), "flood-reduction")
    print ("ospfv3", (procID), "ipv4 area 0")


print ("                                         ")
print ("router ospfv3", (procID))
print ("address-family ipv4 vrf", (vrf))
print ("redistribute bgp 4769")


print ("                                         ")
print ("router bgp 4769")
print ("address-family ipv4 vrf", (vrf))
print ("redistribute connected")
print ("redistribute ospfv3", (procID))