#This script is designed for using the unifi controller.
#To install the unifi controller on an ubuntu 20.04 server, run the following code in the CLI:

# sudo apt-get update
# sudo apt-get install --yes ca-certificates apt-transport-https wget

# echo 'deb https://www.ui.com/downloads/unifi/debian stable ubiquiti' | sudo tee /etc/apt/sources.list.d/100-ubnt-unifi.list
# sudo wget -O /etc/apt/trusted.gpg.d/unifi-repo.gpg https://dl.ui.com/unifi/unifi-repo.gpg

# sudo apt update
# sudo apt install --yes openjdk-8-jre-headless unifi


import requests
import json
from pprint import pprint

requests.packages.urllib3.disable_warnings()
# set up connection parameters in a dictionary
controller = {"ip": "3.142.255.165", "port": "8443"}

# set REST API headers
headers = {"Accept": "application/json",
           "Content-Type": "application/json"}
# set URL parameters
loginUrl = 'api/login'
url = f"https://{controller['ip']}:{controller['port']}/{loginUrl}"
# set username and password
body = {
    "username": "bclayton91",
    "password": "BRan!@n12345"
}
# Open a session for capturing cookies
session = requests.Session()
# login
response = session.post(url, headers=headers,
                        data=json.dumps(body), verify=False)

# parse response data into a Python object
api_data = response.json()
print("/" * 50)
pprint(api_data)
print('Logged in!')
print("/" * 50)

# Set up to get site name
getSitesUrl = 'api/self/sites'
url = f"https://{controller['ip']}:{controller['port']}/{getSitesUrl}"
response = session.get(url, headers=headers,
                       verify=False)
api_data = response.json()
print("/" * 50)
siteslist = api_data['data']

#pprint (siteslist)

for site in siteslist:
    print ("Gathering site information")
    print ("-" * 50)
    print (f'Site name: {site["desc"]}')
    print (f'Your role: {site["role"]}')
    if site["desc"] == 'Brandon & Samantha Home':
        print ("This is your headquarters site")
    else:
        print ("This is a spoke site")
    print ("*" * 50)
    