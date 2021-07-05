from backend.NGSI_Interpreter.POST_Subscription import Create_Subscription

#Creating json file for testing
from backend.NGSI_Interpreter.Save_Entity_To_DB import Save_Subscriptoin_To_Db

payload = {
  "description": "Notify me on AirQualityObserved:AirTemperature changes",

  "type": "Subscription",
  "entities": [{"type": "AirQualityObserved"}],
    "watchedAttributes": ["airTemperature"],
  "notification": {
    "attributes": ["airTemperature"],
    "format": "keyValues",
    "endpoint": {
      "uri": "http://localhost:3000/app/monitor",
      "accept": "application/json"
    }
  },
   "@context": "https://fiware.github.io/tutorials.Step-by-Step/tutorials-context.jsonld"
}

# Creating the entity
broker_response = Create_Subscription(payload)
Save_Subscriptoin_To_Db(payload)
print(broker_response.status_code, broker_response.text)
