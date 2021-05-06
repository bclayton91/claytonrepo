from netmiko import ConnectHandler
import time
import datetime
import os
from labDevices import Lejeune_Devices, Foster_Devices, Pendleton_Devices

date_object = datetime.date.today()

def backup_config_CLJN(self):
    
    try:
        os.makedirs('C:/GitExample1/Git/Python Programs/Netmiko/Backups/CLJN')
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
        
        
        
        fh=open(f'C:/GitExample1/Git/Python Programs/Netmiko/Backups/CLJN/{self["secret"]} {date_object} configuration.txt','w')
        fh.write(data)
        fh.close()
        print(f'Configuration generated successfully')
        print("")
        time.sleep(0.25)

    except:
        print(f'Could not connect to device: {self["secret"]}')

def backup_config_FSTR(self):
    
    try:
        os.makedirs('C:/GitExample1/Git/Python Programs/Netmiko/Backups/FSTR')
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
        
        
        
        fh=open(f'C:/GitExample1/Git/Python Programs/Netmiko/Backups/FSTR/{self["secret"]} {date_object} configuration.txt','w')
        fh.write(data)
        fh.close()
        print(f'Configuration generated successfully')
        print("")

    except:
        print(f'Could not connect to device: {self["secret"]}')    

def backup_config_PNDL(self):
    
    try:
        os.makedirs('C:/GitExample1/Git/Python Programs/Netmiko/Backups/PNDL')
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
        
        
        
        fh=open(f'C:/GitExample1/Git/Python Programs/Netmiko/Backups/PNDL/{self["secret"]} {date_object} configuration.txt','w')
        fh.write(data)
        fh.close()
        print(f'Configuration generated successfully')
        print("")

    except:
        print(f'Could not connect to device: {self["secret"]}')       

for device in Lejeune_Devices:
    backup_config_CLJN(device)
for device in Foster_Devices:
    backup_config_FSTR(device)
for device in Pendleton_Devices:
    backup_config_PNDL(device)

print("")
print("/"*50)
print("Configurations stored in the following directory:")
print("C:/GitExample1/Git/Python Programs/Netmiko/Backups")
print("")

