import json

Data= '''
{"SiteVariables":
[
    {
        "Site":"Test1",
        "Site_Id":"77",
        "Primary_Hub":"192.168.10.4",
        "Secondary_Hub":"192.168.11.4",
        "Tertiary_Hub":"192.168.12.4",
        "Community_String":"123:101",
        "get-vpnrtr-config":"True"
    },

    {
        "Site":"Test2",
        "Site_Id":"78",
        "Primary_Hub":"192.168.10.4",
        "Secondary_Hub":"192.168.11.4",
        "Tertiary_Hub":"192.168.12.4",
        "Community_String":"123:101",
        "get-vpnrtr-config":"True"
    },

    {
        "Site":"Test3",
        "Site_Id":"79",
        "Primary_Hub":"192.168.10.4",
        "Secondary_Hub":"192.168.11.4",
        "Tertiary_Hub":"192.168.12.4",
        "Community_String":"123:101",
        "get-vpnrtr-config":"False"
    }
]
}
'''
sitevars=json.loads(Data)
Vars=sitevars["SiteVariables"]

