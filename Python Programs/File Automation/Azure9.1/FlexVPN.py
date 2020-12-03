import json
from pprint import pprint
 
##Create file variables##
mission="GT-2053-20"
filename=f'{mission} Document'
 
##Input Mission Data##
Data="""
[
{"Terminal":"7615700",
"gt":"GT-2053-20",
"vrf":"RHN5SEP3",
"loopback":"10506"}
]
"""
 
##Load JSON Data into Python as dictionary/list##
Nodes=json.loads(Data)
 
## print (type(Nodes))  **Verifying python collection type##
 
fh = open(f'{filename}.txt', 'w')
 
##pprint (Nodes)  **Verifying data formatting
 
##Create attribute lists##
for node in Nodes:
    fh.write("aaa attribute list  ")
    fh.write(node["Terminal"])
    fh.write("\n")
    fh.write("  attribute type interface-config ")
    fh.write('"desc AUTO-TUNNEL - ')
    fh.write(node["gt"])
    fh.write(" - ")
    fh.write(node["Terminal"])
    fh.write('"')
    fh.write("\n")
    fh.write('  attribute type interface-config "vrf forwarding ')
    fh.write(node["vrf"])
    fh.write('"')
    fh.write("\n")
    fh.write('  attribute type interface-config "ip unnumbered Loopback ')
    fh.write(node["loopback"])
    fh.write('"')
    fh.write("\n")
    fh.write('  attribute type interface-config "ipv6 enable"')
    fh.write("\n")
    fh.write('  attribute type  interface-config "ospfv3 1 ipv4 area 0"')
    fh.write("\n")
    fh.write('  attribute type interface-config "service-policy output PMAP_IVPN_SHAPE_OUT_3MB"')    
    fh.write("\n")
    fh.write("\n")
    
##Create crypto policy##    
    fh.write("crypto ikev2 authorization policy ")
    fh.write(node["Terminal"])
    fh.write("\n")
    fh.write("  aaa attribute list ")
    fh.write(node["Terminal"])
    fh.write("\n")
    fh.write("\n")
    fh.write("exit")
    fh.write("\n")
    fh.write("\n")
    fh.write("\n")
 
##Create teardown procedure##
fh.write("!!!!!!!!!!!!!!!!!! TEARDOWN  !!!!!!!!!!!!!!!!!!!!!!!!!!")
for node in Nodes:
    fh.write("\n")
    fh.write("\n")
    fh.write("no crypto ikev2 authorization policy ")
    fh.write(node["Terminal"])
    fh.write("\n")
    fh.write("no aaa attribute list ")
    fh.write(node["Terminal"])