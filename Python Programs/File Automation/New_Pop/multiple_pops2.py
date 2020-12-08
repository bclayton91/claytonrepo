#import required libraries
from jinja2 import Environment, FileSystemLoader
import json 
from site_data import Sites, Data


#This line uses the current directory 
file_loader = FileSystemLoader('.')

# Load the enviroment
env = Environment(loader=file_loader)

# Create configuration generator functions
def get_xper_config():
    if site["get_xper_config"] == "True":
            output = template.render(
            third_oct=site["third_octet"],
            Gait_ip=site["Gait_ip"],
            Disa_ip=site["Disa_ip"],
            CCSD=site["ccsd"],
            csc=site["csc_subnet"],
            hostname=site["hostname"],
            username=site["username"],
            password=site["password"])

            doc_name = f'{site["hostname"]} xper'
            fh=open(f'{doc_name}.txt', 'w')
            fh.write(output)
            fh.close()
    
    else:
        print (f'skipping {site["hostname"]} xper configuration')




def get_xaxs_config():
    if site["get_xaxs_config"]== "True":
        output2 = template2.render(
        username=site["username"],
        password=site["password"],
        hostname=site["hostname"], 
        third_oct=site["third_octet"])

        doc_name = f'{site["hostname"]} xaxs'
        fh=open(f'{doc_name}.txt', 'w')
        fh.write(output2)
        fh.close()

    else:
        print (f'skipping {site["hostname"]} xaxs configuration')

    

def get_pcr_config():
    if site["get_pcr_config"]== "True":
        output3 = template3.render(
        hostname=site["hostname"], 
        third_oct=site["third_octet"])

        doc_name = f'{site["hostname"]} PCR Configuration'
        fh=open(f'{doc_name}.txt', 'w')
        fh.write(output3)
        fh.close()

    else:
        print (f'skipping {site["hostname"]} pcr configuration')

def get_snmpc_config():
    if site["get_snmpc_config"]== "True":
        output4 = template4.render(
        hostname=site["hostname"], 
        third_oct=site["third_octet"])
    
        doc_name = f'{site["hostname"]} SNMPc Configuration'
        fh=open(f'{doc_name}.txt', 'w')
        fh.write(output4)
        fh.close()

    else:
        print (f'skipping {site["hostname"]} snmpc configuration')

#implement For loop to generate multiple configurations
for site in Sites:

#Call functions to generate configurations 
    template = env.get_template('xper.j2')
    get_xper_config()

    template2 = env.get_template('xaxs.j2')
    get_xaxs_config()

    template3 = env.get_template('rr.j2')
    get_pcr_config()

    template4 = env.get_template('snmpc_vpn.j2')
    get_snmpc_config()

fh=open("Retained-Vars.txt", 'w')
fh.write(Data)
fh.close()