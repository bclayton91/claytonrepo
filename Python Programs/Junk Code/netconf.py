from ncclient import manager 
router = {"host": "192.168.3.1","port":"22","username":"bclayton7043", "password":"temporary1"}

with manager.connect(host=router["host"],port=router["port"],username=router["username"],password=router["password"]) as m:
    for capability in m.server_capabilities:
        print ("*"*50)
        print(capability)
    m.close_session()

