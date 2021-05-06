import shutil

source="C:/GitExample1/Git/Python Programs/Netmiko"
destination="C:/GitExample1/Git/Python Programs/NewFolder"

try:
    shutil.rmtree(destination)
    print("Deleting folder, creating new one")
    print ("*"*75)
    print("")
except:
    print("Creating new folder")
    print ("*"*75)
    print("")    

    
shutil.copytree(source,destination)
print(f'Backup configurations copied to directory: {destination}')
print("!"*50)
