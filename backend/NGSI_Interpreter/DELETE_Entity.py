import requests

from backend.NGSI_Interpreter.Connection_To_Db import Db_Connect
from backend.NGSI_Interpreter.LoadConfigFile_and_Parameters import CBhost, CBport, DBhost, DBport, DBname

#function DELETE Entity from Context Broker based on specific Entity_ID query
#Example : id ='urn:ngsi-ld:WaterQualityObserved:waterqualityobserved:Sevilla:D1'
Entity_ID = 'urn:ngsi-ld:AirQualityObserved:Airqualityobserved:Sevilla:D1'
db = Db_Connect(DBhost, DBport, DBname)
collection_entities = db['entities']
def Delete_entity_By_ID(Entity_ID):
    entity = requests.delete("http://{}:{}/ngsi-ld/v1/entities/{}".format(CBhost, CBport,Entity_ID))
    return
    return entity

