#### import the manager function from the ncclient extenstion ###
from ncclient import manager 

### create a dictionary of the router you are going to be connecting to ###
router = {"host": "192.168.3.1","port":"22","username":"bclayton7043", "password":"temporary1"}

### create a netconf filter to filter the information you want to receive ###
netconf_filter="""
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet0/2</name>
            </interface>
        </interfaces>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet0/2</name>
            </interface>
        </interfaces-state>
    </filter>
    """

### using the manager function, connect to the router using the router information ###
with manager.connect(host=router["host"],port=router["port"],username=router["username"],
password=router["password"]) as m:

### use the below commands to print out the yang models the router is capable of using ###
    for capability in m.server_capabilities:
        print ("*"*50)
        print(capability)
    m.close_session()