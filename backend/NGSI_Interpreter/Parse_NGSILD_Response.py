import json
#function that parse NGSI-LD Server Response to JSON Format
def Parse_NGSILD_to_JSON(NGSI_MSG):
    json_dict = json.loads(NGSI_MSG.text)
    return json_dict
