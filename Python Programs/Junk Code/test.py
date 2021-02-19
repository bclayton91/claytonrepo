from jinja2 import FileSystemLoader, Environment

file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
template = env.get_template("test.j2")
output = template.render(
    region= "west"
)
print (output)
