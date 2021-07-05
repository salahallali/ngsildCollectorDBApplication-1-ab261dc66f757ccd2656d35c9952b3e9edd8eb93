import requests

url = "http://localhost:8000/entities"

payload = "{\n\t\"id\":\"urn:ngsi-ld:AgriDevice:AgriDSoil:IPex12:00001\",\n\t\"type\":\"AgriDevice\",\n\t\"category\": {\n\t\t\"type\": \"Property\",\n\t\t\"value\": \"Soil\"\n\t},\n\t\"s4ee:deviceName\": {\n\t\t\"type\":\"Property\",\n\t\t\"value\":\"IPex12:00043\"\n\t},\n\t\"s4ee:serialNumber\": {\n\t\t\"type\":\"Property\",\n\t\t\"value\":\"IA0201E16000100043\"\n\t},\n\t\"temperature\": {\n\t\t\"type\":\"Property\",\n\t\t\"value\":13.7\n\t},\n\t\"humidity\": {\n\t\t\"type\":\"Property\",\n\t\t\"value\":15.58\n\t},\n\t\"conductivity\": {\n\t\t\"type\":\"Property\",\n\t\t\"value\":0.23\n\t},\n\t\"s4ee:manufacturerDescription\": {\n\t\t\"type\":\"Property\",\n\t\t\"value\":\"https://www.odins.es/\"\n\t},\n\t\"@context\": [\n\t\t\"http://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld\",\n\t\t{\n\t\t\t\"s4ee\": \"https://ontology.tno.nl/saref4ee/#\"\n\t\t}\n\t]\n}"
headers = {
  'Content-Type': 'application/ld+json',
  'Authorization': 'Token 882fe5c68a7dae8dbd5a9734adacc7912d3d0259',
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response)