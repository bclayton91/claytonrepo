import json

Data= '''
[
    {
        "Site":"I-MEF",
        "Site_Id":"77",
        "Primary_Hub":"192.168.10.4",
        "Secondary_Hub":"192.168.11.4",
        "Tertiary_Hub":"192.168.12.4",
        "Community_String":"123:101",
        "get-vpnrtr-config":"True"
    },
        {
        "Site":"II-MEF",
        "Site_Id":"78",
        "Primary_Hub":"192.168.10.4",
        "Secondary_Hub":"192.168.11.4",
        "Tertiary_Hub":"192.168.12.4",
        "Community_String":"123:101",
        "get-vpnrtr-config":"True"
    }
]
'''
Vars=json.loads(Data)


