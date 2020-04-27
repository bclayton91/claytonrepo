import requests

url = "https://thesurfsupsurfschool.com/"

payload = {}
headers = {
  'Authorization': 'Basic YnJhbmRvbmNsYXl0b25jMGMyQGdtYWlsLmNvbTpUZW1wb3JhcnkxMQ=='
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))