from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('.')
# Load the enviroment
env = Environment(loader=file_loader)

template = env.get_template('jtemplate.j2')

#Create the list of VLANs you want to generate configuration for
vlans = [10,20,30,40,50,60,70,80,90,100]
ip_add=[1,2,3,4,5,6,7,8,9,10]

#Iterate over the list of vlans and print a useable configuration
for vlan in vlans:
    output = template.render(vlan=vlan, ip=ip_add)
    
    print(output)