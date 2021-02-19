import json

router = {
"int"   :"bdi401",
"int_type" : "bdi",                                  #physical or bdi
################################## The following 2 are only used with BDI interfaces ############################
"int2"  :"ethernet-internal 1/0/0",       
"desc"  : "description TO SWITCH G0/18" ,
"bridgedomain" : "401",        
"SI"    : "service-instance 401",                        
#################################################################################################################    
"tag"   : "401",                                    #vlan
"desc2" : "description {{Add description here}}",      #description under interfaces
"procID": "1",                                     #ospfv3 process ID
"vrf"   : "TENANT1",                                   #vrf instance used
"IP"    : "{{insert IP address here}}",           #Ip address of the interface
"routing_protocol":"ospfv3",                           #ospfv3 or bgp
####################################  only use below variables for bgp local connections #######################
"neighbor_ip":"10.108.64.89",
"remote_as":"65970",
"neighbor_desc":"description connection to whoever"
}





