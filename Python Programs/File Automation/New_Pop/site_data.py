import json

#input site data
Data= '''
[
    {
        "hostname":"59SIG-FGAK",
        "Gait_ip":"33.44.166.2",
        "Disa_ip":"33.44.166.1",
        "csc_subnet":"33.44.166.0/30",
        "third_octet":"189",
        "ccsd":"XNA2",
        "get_xper_config": "True",
        "get_xaxs_config": "True",
        "get_pcr_config": "True",
        "get_snmpc_config": "True",
        "username":"gdadmin",
        "password":"GenDyn1234567*("
    },
    {
        "hostname":"NSC-FSNC",
        "Gait_ip":"33.0.2.2",
        "Disa_ip":"33.0.2.1",
        "csc_subnet":"33.0.2.0/30",
        "third_octet":"2",
        "ccsd":"2000",
        "get_xper_config": "True" ,
        "get_xaxs_config": "True" ,
        "get_pcr_config": "True" ,
        "get_snmpc_config": "True" ,
        "username":"gdadmin",
        "password":"GenDyn1234567*("
    },
    {
        "hostname":"NSC-FGGA",
        "Gait_ip":"33.0.3.2",
        "Disa_ip":"33.0.3.1",
        "csc_subnet":"33.0.3.0/30",
        "third_octet":"3",
        "ccsd":"3000",
        "get_xper_config":"True",
        "get_xaxs_config": "True",
        "get_pcr_config": "True",
        "get_snmpc_config": "True",
        "username":"gdadmin",
        "password":"GenDyn1234567*("
    },
    {
        "hostname":"NSC-standalone",
        "Gait_ip":"33.0.1.2",
        "Disa_ip":"33.0.1.1",
        "csc_subnet":"33.0.1.0/30",
        "third_octet":"1",
        "ccsd":"1000",
        "get_xper_config": "True",
        "get_xaxs_config":"False",
        "get_pcr_config":"False",
        "get_snmpc_config":"False",
        "username":"gdadmin",
        "password":"GenDyn1234567*("
    }
]
'''
#deserialize json data into python list
Sites=json.loads(Data)