import sys

from backend.NGSI_Interpreter.Get_Entities import Get_entity_By_ID
from backend.NGSI_Interpreter.Parse_NGSILD_Response import Parse_NGSILD_to_JSON
from backend.NGSI_Interpreter.Save_Entity_To_DB import Save_Entity_To_Db


try:
    ########### tests ##########################
    id ='urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1'
    id_air = 'urn:ngsi-ld:AirQualityObserved:Airqualityobserved:Sevilla:D1'
    req = '?type={}'.format('WaterQualityObserved')
    ###############################################################

    # Example of getting Entity By ID (id or id_air)
    NGSI_Response = Get_entity_By_ID(id_air)

    # Example of getting Entity By Type
    #NGSI_Response = Get_entity_By_Type(req)

    print("Context Broker's Response: ", NGSI_Response)
    #print(NGSI_Response.status_code, NGSI_Response.text)

    entity= Parse_NGSILD_to_JSON(NGSI_Response)
    print(entity)
    #setting Entity ID in the Response file to "_id" instead of "id" to avoid redandency in the Database
    entity['_id'] = entity.pop('id')

    #Saving Entity to MongoDB
    save_entity = Save_Entity_To_Db(entity)
    print('[+] entity saved..........')
except:
    print("Unexpected error:", sys.exc_info()[1])
    pass





