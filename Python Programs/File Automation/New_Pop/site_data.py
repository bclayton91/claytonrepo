import json

#input site data
Data= '''
[
{
"hostname":"Greenville-NC",
"Gait_ip":"33.0.1.2",
"Disa_ip":"33.0.1.1",
"csc_subnet":"33.0.1.0/30",
"third_octet":"1",
"ccsd":"1000",
"username":"gdadmin",
"password":"GenDyn1234567*("
},
{
"hostname":"San-Diego-CA",
"Gait_ip":"33.0.2.2",
"Disa_ip":"33.0.2.1",
"csc_subnet":"33.0.2.0/30",
"third_octet":"2",
"ccsd":"2000",
"username":"gdadmin",
"password":"GenDyn1234567*("
},
{
"hostname":"Charleston-SC",
"Gait_ip":"33.0.3.2",
"Disa_ip":"33.0.3.1",
"csc_subnet":"33.0.3.0/30",
"third_octet":"3",
"ccsd":"3000",
"username":"gdadmin",
"password":"GenDyn1234567*("
}

]
'''
#deserialize json data into python list
Sites=json.loads(Data)