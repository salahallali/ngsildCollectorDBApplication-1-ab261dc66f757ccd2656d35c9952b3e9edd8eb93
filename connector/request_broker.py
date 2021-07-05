import requests
from backend.LoadConfigFile_and_Parameters import CBhost, CBport
def Get_entity_by_id(id):
    respons = requests.get(f"http://{CBhost}:{CBport}/ngsi-ld/v1/entities/{id}")
    return respons


def Get_entity_by_type(type):
    respons = requests.get(f"http://{CBhost}:{CBport}/ngsi-ld/v1/entities?type={type}")
    return respons

def Delete_entity(id):
    respons = requests.delete(f"http://{CBhost}:{CBport}/ngsi-ld/v1/entities/{id}")
    return respons


def Create_entity(payload) :

    respons = requests.post(f"http://{CBhost}:{CBport}/ngsi-ld/v1/entities", json=payload,
                       headers={"Content-Type": "application/ld+json"})
    return respons


def Update_entity(entity):
    respons = requests.post(f"http://{CBhost}:{CBport}/ngsi-ld/v1/entities/{entity['id']}/attrs", json=entity,
                            headers={"Content-Type": "application/ld+json"})
    return respons


#########subscriptions###################

def Get_subscription_by_id(id):
    respons = requests.get(f"http://{CBhost}:{CBport}/ngsi-ld/v1/subscriptions/{id}")
    return respons


def Get_subscriptions():
    respons = requests.get(f"http://{CBhost}:{CBport}/ngsi-ld/v1/subscriptions")
    return respons

def Delete_subscription(id):
    respons = requests.delete(f"http://{CBhost}:{CBport}/ngsi-ld/v1/subscriptions/{id}")
    return respons


def Create_subscription(payload) :

    respons = requests.post(f"http://{CBhost}:{CBport}/ngsi-ld/v1/subscriptions", json=payload,
                       headers={"Content-Type": "application/ld+json"})
    return respons
