#import required libraries
from jinja2 import FileSystemLoader, Environment
import json

#input site data
Data='''
[
    {
    "Terminal":"761500",
    "GT":"GT-2030-20",
    "VRF":"RHN5SEP3",
    "loopback":"10503"
    },
    {
    "Terminal":"761501",
    "GT":"GT-2030-20",
    "VRF":"RHN5SEP3",
    "loopback":"10503"
    }
]
'''
#deserialize json site data into python list
Nodes=json.loads(Data)

#use FileSystemLoader in the current directory
file_loader=FileSystemLoader('.')

#load Environment
env=Environment(loader=file_loader)

#create configuration generator function
def get_config():
    output=template.render(
    Terminal=Node["Terminal"],
    GT=Node["GT"],
    VRF=Node["VRF"],
    loopback=Node["loopback"])
    
    doc_name = f'{Node["GT"]} Terminal {Node["Terminal"]} ivpn9.1'
    fh=open(f'{doc_name}.txt', 'w')
    fh.write(output)
    fh.close()

#use For loop to generate configs 
for Node in Nodes:
    template=env.get_template("ivpn.j2")
    get_config()





