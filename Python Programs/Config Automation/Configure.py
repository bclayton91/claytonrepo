### Import required libraries
from pprint import pprint
from jinja2 import Environment, FileSystemLoader
from Vars import Vars, Data
import time

##Load your environment
file_loader = FileSystemLoader('Templates')
env=Environment(loader=file_loader)

##Define your function
def get_vpnrtr_config(self):
    if self["get-vpnrtr-config"]=="True":        
        print("Generating vpn rtr config")
        print("/"*50)
        print(" ")
        time.sleep(0.75)
        output=template.render(
        Site=self["Site"],
        Site_Id=self["Site_Id"],
        Primary_Hub=self["Primary_Hub"],
        Secondary_Hub=self["Secondary_Hub"],
        Tertiary_Hub=self["Tertiary_Hub"],
        Community_String=self["Community_String"])

        docname=(f"{self['Site']}-VPN-RTR-CONFIG")
        fh=open(f'Configurations/{docname}.txt', 'w')
        fh.write(output)
        fh.close()

    else:
        print ("Skipping vpn router configuration")
        print ("-"*50)
        print (" ")
        time.sleep(0.75)

print ("Loading VPNRTR Template")
time.sleep(0.75)
print ("*"*50)
print (" ")

##Using 'for' loop, call the function against each site
for Var in Vars:
    template=env.get_template('VPNRTR.j2')
    get_vpnrtr_config(Var)

print( "Generating variable file")
print("*"*50)
time.sleep(1)
print(" ")
print("Completed, files stored in Configurations folder")
print("_"*50)

##Create documents and place them in the "Configurations" folder
fh=open('Configurations/Variables used.txt', 'w')
fh.write(Data)
fh.close()
