  
import requests
import json
from pprint import pprint 

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# set up connection parameters in a dictionary
router = {"ip": "ios-xe-mgmt.cisco.com", "port": "9443",
          "user": "developer", "password": "C1sco12345"}

# set REST API headers
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface"
# print(url)

response = requests.get(url, headers=headers, auth=(
    router['user'], router['password']), verify=False)


api_data = response.json()
print("*" * 50)
#print("*" * 50)
#if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
#    print('Interface is up')
#else: print("interface is down")
pprint (type(api_data['Cisco-IOS-XE-interfaces-oper:interface']))
#print (f"Name: {api_data['name']}")
#pprint (api_data['Cisco-IOS-XE-interfaces-oper:interface'])
for int_name in api_data['Cisco-IOS-XE-interfaces-oper:interface']:
    pprint (int_name['name'])
    pprint (int_name['description'])
    if int_name['admin-status']=='if-state-up':
        pprint ('The interface is up')
    else: pprint ('The interface is down')
    pprint ("*"*25)


pprint (api_data)

