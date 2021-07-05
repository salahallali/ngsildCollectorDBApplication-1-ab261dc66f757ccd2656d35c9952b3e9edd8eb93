import sys

from backend.NGSI_Interpreter.DELETE_Entity import Delete_entity_By_ID
    ########### tests ######################
id ='urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1'
id_air = 'urn:ngsi-ld:AirQualityObserved:Airqualityobserved:Sevilla:D1'
    ###############################################################
try:
    #Deleting Entity from MongoDB
    delet_entity = Delete_entity_By_ID(id)
    print('[+] entity DELETED..........')
except:
    print("Unexpected error:", sys.exc_info()[1])
    pass







