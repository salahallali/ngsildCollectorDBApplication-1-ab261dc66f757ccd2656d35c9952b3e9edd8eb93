import requests
from backend.NGSI_Interpreter.LoadConfigFile_and_Parameters import CBhost, CBport




#function returns Entity description based on specific Entity_ID query
#Example : id ='urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1'
def Get_entity_By_ID(Entity_ID):
    entity = requests.get("http://{}:{}/ngsi-ld/v1/entities/{}".format(CBhost, CBport,Entity_ID))
    return entity

#function returns Entity description based on specific Entity_Type query
#Example: req = '?type={}'.format('WaterQualityObserved')
def Get_entity_By_Type(Entity_Type):
    entity = requests.get("http://{}:{}/ngsi-ld/v1/entities/{}".format(CBhost, CBport,Entity_Type))
    return entity

#function returns Entity description based on generic Entity query
#Example: req = '?{}'.format(Request)
def Get_entity_By_Query(Entity_Query):
    entity = requests.get("http://{}:{}/ngsi-ld/v1/entities/{}".format(CBhost, CBport,Entity_Query))
    return entity