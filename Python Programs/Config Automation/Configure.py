from pprint import pprint
from jinja2 import Environment, FileSystemLoader
from Vars import Vars, Data
import time

file_loader = FileSystemLoader('Templates')

env=Environment(loader=file_loader)

def get_vpnrtr_config(site):
    if site["get-vpnrtr-config"]=="True":
        print("Generating vpn rtr config")
        time.sleep(1)
        output=template.render(
        Site=site["Site"],
        Site_Id=site["Site_Id"],
        Primary_Hub=site["Primary_Hub"],
        Secondary_Hub=site["Secondary_Hub"],
        Tertiary_Hub=site["Tertiary_Hub"])
        docname=(f"{site['Site']}-VPN-RTR-CONFIG")
        fh=open(f'Configurations/{docname}.txt', 'w')
        fh.write(output)
        fh.close()

    else:
        print ("Skipping vpn router configuration")
        time.sleep(1)

for Var in Vars:
    template=env.get_template('VPNRTR.j2')
    get_vpnrtr_config(Var)

print ("Generating variable file")
fh=open('Configurations/Variables used.txt', 'w')
fh.write(Data)

