#Creating json file for testing
from backend.NGSI_Interpreter.UBDATE_Entity import Update_entity

payload = {

      "airTempirature":{"type":"Property", "value": 3}
}
id_air = 'urn:ngsi-ld:AirQualityObserved:Airqualityobserved:Sevilla:D1'
# Creating the entity
broker_response = Update_entity(payload, id_air)

print(broker_response.status_code, broker_response.text)

