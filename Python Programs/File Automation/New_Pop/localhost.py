from jinja2 import Environment, FileSystemLoader

#set variables 
zipname='TAO-LOH'
Id='TAO-LOH'
third_octet='193'
disa_subnet='33.40.74.4/30'
ccsd='71WL'
location='Lima_OH'
region='conus_east'


#This line uses the current directory
file_loader = FileSystemLoader('.')

# Load the enviroment
env = Environment(loader=file_loader)
template = env.get_template('localhost-temp.j2'
)
#Apply the veriables
output = template.render(

zipname=zipname,
id=Id,
third_oct=third_octet,
disa_subnet=disa_subnet,
CCSD=ccsd,
location=location,
region=region

)

#Create document
doc_name = f'{zipname} vars'
fh=open(f'{doc_name}.txt', 'w')
fh.write(output)
fh.close()
