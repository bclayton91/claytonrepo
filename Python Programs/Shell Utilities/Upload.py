import shutil

source="C:/GitExample1/Git/Python Programs/Netmiko"
destination="C:/GitExample1/Git/Python Programs/NewFolder"

try:
    shutil.rmtree(destination)
except:
    shutil.copytree(source,destination)
    print("Folder created")