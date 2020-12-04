from jinja2 import Environment, FileSystemLoader

#set variables 
hostname='Test_Pop'
Gait_ip='33.0.44.2'
Disa_ip='33.0.44.1'
csc_subnet='33.0.44.0/30'
third_octet='158'
ccsd='7M44'
username='gdadmin'
password='GenDyn1234567*('

#This line uses the current directory
file_loader = FileSystemLoader('.')

# Load the enviroment
env = Environment(loader=file_loader)
template = env.get_template('xper.j2'
)
#Apply the veriables
output = template.render(

third_oct=third_octet,
Gait_ip=Gait_ip,
Disa_ip=Disa_ip,
CCSD=ccsd,
csc=csc_subnet,
hostname=hostname,
username=username,
password=password

)
#Create document
doc_name = f'{hostname} xper'
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

username=username,
password=password,
hostname=hostname, 
third_oct=third_octet

)
#Create document
doc_name = f'{hostname} xaxs'
fh=open(f'{doc_name}.txt', 'w')
fh.write(output2)
fh.close()