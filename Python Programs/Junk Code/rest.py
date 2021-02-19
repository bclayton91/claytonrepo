import json 

json_string= """
{
    "researcher":{
        "name":"ford",
        "species":"idk"
    }
}
"""
print (type(json_string))

my_json=json.loads(json_string)
print (type(my_json))