from Exscript.util.interact import read_login
from Exscript.protocols import SSH2

## Create file name variable and set the host ip to your tftp server binding
file_name = "clayton_edge-confg"
host_ip= "192.168.3.30"

account = read_login()              
conn = SSH2()                       
conn.connect('192.168.3.1')     
conn.login(account)  


       
conn.execute('copy tftp startup-config')
conn.execute("192.168.3.30")
conn.execute("startup-config")
conn.execute('clayton_edge-confg')
print (conn.response)


conn.send('exit\r')               
conn.close()  