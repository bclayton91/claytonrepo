import json
from pprint import pprint 
import requests

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# set up connection parameters in a dictionary
router = {"ip": "ios-xe-mgmt.cisco.com", "port": "9443",
          "user": "developer", "password": "C1sco12345"}

# set REST API headers
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

module = "Cisco-IOS-XE-interfaces-oper:interfaces/interface"

url = f"https://{router['ip']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=loopback21"

payload = {
   "interface": [
    {
      "name": "Loopback21",
      "description": "Configured via restconf - B.Clayton",
      "type": "iana-if-type:softwareLoopback",
      "enabled": "true",
      
    }
  ]
 }

data=json.dumps(payload)

response = requests.patch(url, headers=headers, data=data ,auth=(router['user'], router['password']), verify=False)

api_data=response.json()

if (response.status_code == 204):
   print("Successfully updated interface")
else:
   print("Issue with updating interface")

print (api_data)