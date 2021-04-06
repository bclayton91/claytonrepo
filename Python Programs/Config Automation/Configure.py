from pprint import pprint
from jinja2 import Environment, FileSystemLoader
from Vars import Vars, Data
import time

file_loader = FileSystemLoader('Templates')

env=Environment(loader=file_loader)

def get_vpnrtr_config():
    if Var["get-vpnrtr-config"]=="True":
        print("Generating vpn rtr config")
        time.sleep(1)
        output=template.render(
        Site=Var["Site"],
        Site_Id=Var["Site_Id"],
        Primary_Hub=Var["Primary_Hub"],
        Secondary_Hub=Var["Secondary_Hub"],
        Tertiary_Hub=Var["Tertiary_Hub"])
        docname=(f"{Var['Site']}-VPN-RTR-CONFIG")
        fh=open(f'{docname}.txt', 'w')
        fh.write(output)
        fh.close()

    else:
        print ("Skipping vpn router configuration")
        time.sleep(1)

for Var in Vars:
    template=env.get_template('VPNRTR.j2')
    get_vpnrtr_config()

fh=open('Variables used.txt', 'w')
fh.write(Data)