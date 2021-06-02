from netmiko import ConnectHandler
import time
import datetime
import os
from labDevices import Lejeune_Devices, Foster_Devices, Pendleton_Devices

date_object = datetime.date.today()
month=date_object.strftime("%B")
def backup_configs(self, HUB):
    
    try:
        path=f'C:/GitExample1/Git/Python Programs/Netmiko/Backups/{HUB}/{month}/{date_object}'
        os.makedirs(path)
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
        time.sleep(0.25)
        
        
        
        fh=open(f'C:/GitExample1/Git/Python Programs/Netmiko/Backups/{HUB}/{month}/{date_object}/{self["secret"]} {date_object} configuration.txt','w')
        fh.write(data)
        fh.close()
        print(f'Configuration generated successfully')
        print("")
        time.sleep(0.25)

    except:
        print(f'Could not connect to device: {self["secret"]}')


for device in Lejeune_Devices:
    backup_configs(device, 'CLJN')
for device in Foster_Devices:
    backup_configs(device, 'FSTR')
for device in Pendleton_Devices:
    backup_configs(device, 'PNDL')

print("")
print("/"*50)
print("Configurations stored in the following directory:")
print(f"C:/GitExample1/Git/Python Programs/Netmiko/Backups/{month}")
print("")

