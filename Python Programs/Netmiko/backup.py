from netmiko import ConnectHandler
import time
import datetime
import os
from labDevices import Network_Devices

date_object = datetime.date.today()

def backup_config(self):
    
    try:
        os.makedirs(f'C:/GitExample1/Git/Python Programs/Netmiko/Backups')
        print("Creating Directory")
        print("*"*50)
        print("")
        print("")
    except:
        
        print("-"*50)
        print("")
    
    try:
        ssh=ConnectHandler(**self)
        ssh.enable()
        cmd="Show run"
        data=(ssh.send_command(cmd))
        print(f"Connecting to device: {self['secret']}")
        print ("*"*50)
        time.sleep(0.5)
        
        
        
        fh=open(f'C:/GitExample1/Git/Python Programs/Netmiko/Backups/{self["secret"]} {date_object} configuration.txt','w')
        fh.write(data)
        fh.close()
        print(f'Configuration generated successfully')
        print("")

    except:
        print(f'Could not connect to device: {self["secret"]}')

        
    

for device in Network_Devices:
    backup_config(device)

print("")
print("/"*50)
print("Configurations stored in the following directory:")
print("C:/GitExample1/Git/Python Programs/Netmiko/Backups")
print("")

