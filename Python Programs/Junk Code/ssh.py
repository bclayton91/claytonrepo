from Exscript.util.interact import read_login
from Exscript.protocols import SSH2

account = read_login()              
conn = SSH2()                       
conn.connect('192.168.3.1')     
conn.login(account)  

## conn.execute('terminal length 0')    
conn.execute("terminal length 0")
       
conn.execute('show ip route')
print (conn.response)

conn.execute('show version')
print (conn.response)

conn.send('exit\r')               
conn.close()  