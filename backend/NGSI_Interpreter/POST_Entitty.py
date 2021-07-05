import requests
url = "http://155.54.210.149:1027/ngsi-ld/v1/entities"
headers = {
  'Accept': 'application/ld+json',
  'Content-Type': 'application/ld+json',
  'Content-Type': 'text/plain'
}
#function that Add Entities To Context Broker based on ssructred Json file returns Context Broker Response
def Create_entity(payload) :

    from backend.NGSI_Interpreter.LoadConfigFile_and_Parameters import CBport
    from backend.NGSI_Interpreter.LoadConfigFile_and_Parameters import CBhost
    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text.encode('utf8'))