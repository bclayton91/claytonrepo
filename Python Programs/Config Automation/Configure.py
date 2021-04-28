### Import required libraries
from pprint import pprint
from jinja2 import Environment, FileSystemLoader
from Vars import Vars, Data
import time
import os

##Load your environment
file_loader = FileSystemLoader('C:\GitExample1\Git\Python Programs\Config Automation\Templates')
env=Environment(loader=file_loader)

##Define your function
def get_vpnrtr_config(self):
    if self["get-vpnrtr-config"]=="True":        
        print(f'Generating vpn rtr config for site {self["Site"]}')
        print("/"*50)
        print(" ")
        time.sleep(0.5)
        output=template.render(
        Site=self["Site"],
        Site_Id=self["Site_Id"],
        Primary_Hub=self["Primary_Hub"],
        Secondary_Hub=self["Secondary_Hub"],
        Tertiary_Hub=self["Tertiary_Hub"],
        Community_String=self["Community_String"])

        docname=(f"{self['Site']}-VPN-RTR-CONFIG")
        try:
            fh=open(f'C:\GitExample1\Git\Python Programs\Config Automation\Configurations\{docname}.txt', 'w')
            fh.write(output)
            fh.close()
        except:
            os.makedirs('C:\GitExample1\Git\Python Programs\Config Automation\Configurations')
            fh=open(f'C:\GitExample1\Git\Python Programs\Config Automation\Configurations\{docname}.txt', 'w')
            fh.write(output)
            fh.close()


    else:
        print (f'Skipping vpn router configuration for site {self["Site"]}')
        print ("-"*50)
        print (" ")
        time.sleep(0.5)

print ("Loading VPNRTR Template")
time.sleep(0.5)
print ("*"*50)
print (" ")

##Using 'for' loop, call the function against each site
for Var in Vars:
    template=env.get_template('VPNRTR.j2')
    get_vpnrtr_config(Var)

print( "Generating variable file")
print("*"*50)
time.sleep(.5)
print(" ")
print("Completed, files stored in Configurations folder")
print("_"*50)

##Create documents and place them in the "Configurations" folder
fh=open('C:\GitExample1\Git\Python Programs\Config Automation\Configurations\Variables used.txt', 'w')
fh.write(Data)
fh.close()
