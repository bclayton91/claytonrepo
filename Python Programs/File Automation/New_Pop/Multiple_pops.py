#import required libraries
from jinja2 import Environment, FileSystemLoader
import json 

# Set individual site variables
Data= '''
[
{
"hostname":"Site1",
"Gait_ip":"33.0.1.2",
"Disa_ip":"33.0.1.1",
"csc_subnet":"33.0.1.0/30",
"third_octet":"1",
"ccsd":"1000",
"username":"gdadmin",
"password":"GenDyn1234567*("
},
{
"hostname":"Site2",
"Gait_ip":"33.0.2.2",
"Disa_ip":"33.0.2.1",
"csc_subnet":"33.0.2.0/30",
"third_octet":"2",
"ccsd":"2000",
"username":"gdadmin",
"password":"GenDyn1234567*("
},
{
"hostname":"Site3",
"Gait_ip":"33.0.3.2",
"Disa_ip":"33.0.3.1",
"csc_subnet":"33.0.3.0/30",
"third_octet":"3",
"ccsd":"3000",
"username":"gdadmin",
"password":"GenDyn1234567*("
}

]
'''

#Deserialize json data into python dictionary 
Sites=json.loads(Data)

#implement For loop to generate multiple configurations
for site in Sites:

#This line uses the current directory
    file_loader = FileSystemLoader('.')

# Load the enviroment
    env = Environment(loader=file_loader)
    template = env.get_template('xper.j2')
    
#Apply the veriables
    output = template.render(

    third_oct=site["third_octet"],
    Gait_ip=site["Gait_ip"],
    Disa_ip=site["Disa_ip"],
    CCSD=site["ccsd"],
    csc=site["csc_subnet"],
    hostname=site["hostname"],
    username=site["username"],
    password=site["password"]

    )
#Create document
    doc_name = f'{site["hostname"]} xper'
    fh=open(f'{doc_name}.txt', 'w')
    fh.write(output)
    fh.close(

    )
#Now create the Switch config 
    env = Environment(loader=file_loader)
    template2 = env.get_template('xaxs.j2'
    )
#Apply the veriables
    output2 = template2.render(

    username=site["username"],
    password=site["password"],
    hostname=site["hostname"], 
    third_oct=site["third_octet"]

    )
#Create document
    doc_name = f'{site["hostname"]} xaxs'
    fh=open(f'{doc_name}.txt', 'w')
    fh.write(output2)
    fh.close()

#Now create the PCR config 
    env = Environment(loader=file_loader)
    template3 = env.get_template('rr.j2'
    )

#Apply the veriables
    output3 = template3.render(

    hostname=site["hostname"], 
    third_oct=site["third_octet"]

    )
#Create document
    doc_name = f'{site["hostname"]} PCR Configuration'
    fh=open(f'{doc_name}.txt', 'w')
    fh.write(output3)
    fh.close()

#Now create the SNMPc config 
    env = Environment(loader=file_loader)
    template4 = env.get_template('snmpc_vpn.j2'
    )

#Apply the veriables
    output4 = template4.render(

    hostname=site["hostname"], 
    third_oct=site["third_octet"]

    )
#Create document
    doc_name = f'{site["hostname"]} SNMPc Configuration'
    fh=open(f'{doc_name}.txt', 'w')
    fh.write(output4)
    fh.close()