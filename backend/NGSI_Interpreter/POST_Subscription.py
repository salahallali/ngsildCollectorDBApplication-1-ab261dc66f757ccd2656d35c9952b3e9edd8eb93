import requests


#function that Add Sbsription To Context Broker based on ssructred Json file returns Context Broker Response
def Create_Subscription(payload) :

    from backend.NGSI_Interpreter.LoadConfigFile_and_Parameters import CBport
    from backend.NGSI_Interpreter.LoadConfigFile_and_Parameters import CBhost
    respons = requests.post("http://{}:{}/ngsi-ld/v1/subscriptions/".format(CBhost, CBport), json=payload,
                       headers={"Content-Type": "application/ld+json"})
    from backend.NGSI_Interpreter.Save_Entity_To_DB import Save_Subscriptoin_To_Db
    Save_Subscriptoin_To_Db(payload)
    return respons