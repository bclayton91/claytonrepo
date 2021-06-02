from netmiko import ConnectHandler
import time
import sys
sys.path.insert(1, "C:/GitExample1/Git/Python Programs/Netmiko")
from labDevices import Lejeune_Devices, Foster_Devices, Pendleton_Devices


#Open doc containing ACL
fh=open("C:/GitExample1/Git/Python Programs/Netmiko/Config/acl.txt", "r")
commands=fh.read()


def configacl(self):
    try:
        ssh=ConnectHandler(**self)
        ssh.enable()
        result=(ssh.send_config_set(commands.split("\n")))
        print(f"{self['secret']} configured successfully")
        print("-"*70)
        print("")
        time.sleep(0.5)
    
    except: 
        print (f"Configuration not applied to device: {self['secret']}")
        print("-"*70)
        print("")
        time.sleep(0.5)



     
for device in Lejeune_Devices:
    configacl(device)
for device in Foster_Devices:
    configacl(device)
for device in Pendleton_Devices:
    configacl(device)

print ("Device configuration complete")
print ("@"*70)