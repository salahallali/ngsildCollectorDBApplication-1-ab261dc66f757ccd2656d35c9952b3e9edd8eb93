import requests


#function that Update Entitie on Context Broker based on structred Json file and an ID of the entity want to be modified
# returns Context Broker Response
from backend.NGSI_Interpreter.Save_Entity_To_DB import Save_Entity_To_Db


def Update_entity(payload, id) :

    from backend.NGSI_Interpreter.LoadConfigFile_and_Parameters import CBport
    from backend.NGSI_Interpreter.LoadConfigFile_and_Parameters import CBhost
    respons = requests.patch("http://{}:{}/ngsi-ld/v1/entities/{}/attrs".format(CBhost, CBport,id), json=payload,
                       headers={"Content-Type": "application/json"})
    from backend.NGSI_Interpreter.Get_Entities import Get_entity_By_ID
    updated_entity = Get_entity_By_ID(id)
    # Saving Entity to MongoDB
    from backend.NGSI_Interpreter.Tests_Getting_and_Saving_Entities import entity
    save_entity = Save_Entity_To_Db(entity)
    return respons