

# import pymodm
# from pymodm import connect, fields, MongoModel, EmbeddedMongoModel
# from pymongo import MongoClient






# function for saving entities (JSON File) into "entities" collection in MongoDB Database
import datetime
import json

from backend.Connection_To_Db import Db_Connect
from backend.LoadConfigFile_and_Parameters import DBhost, DBport, DBname, DBpwd, DBuser


def Save_Entity_To_Db(entity):
    # Connection to Database in specific collection "entities"
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    collection_entities = db['entities']
    if type(entity) is list:
        for entity_i in entity:
            #setting Entity ID in the Response file to "_id" instead of "id" to avoid redandency in the Database
            entity_i['_id'] = entity_i.pop('id')
            collection_entities.save(entity_i)
            entity_i['id'] = entity_i.pop('_id')
    else:
        entity['_id'] = entity.pop('id')
        collection_entities.save(entity)
        entity['id'] = entity.pop('_id')
    return 0


def Delete_Entity_from_Db(id,filter):
    # Connection to Database in specific collection "entities"
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    collection_entities = db['entities']
    if filter == 'type':
        return collection_entities.delete_many({'type': id})
    else:
        return collection_entities.delete_one({'_id': id})



def Update_Entity_On_Db(entity):
    # Connection to Database in specific collection "entities"
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    collection_entities = db['entities']
    #setting Entity ID in the Response file to "_id" instead of "id" to avoid redandency in the Database
    entity['_id'] = entity.pop('id')
    collection_entities.update({'_id':entity['_id']}, {"$set": entity}, upsert=False)
    entity['id'] = entity.pop('_id')
    return 0

def Save_Notification_To_Db(notification, collection):
    # Connection to Database in specific collection "entities"
    try:
        print('\n saving notification .................\n')
        db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
        collection_notifications = db[collection]
        collection_notifications.save(notification)
        update_service({"_id":notification["data"][0]["id"], "notifiedAt": datetime.strptime(notification["notifiedAt"],
                                                                                             '%Y-%m-%dT%H:%M:%SZ')})
        Update_Entity_On_Db(notification['data'][0])
        print(f"\n[+] notification '{notification['id']}' saved successfully ^^\n")
    except:
        print(f"\n[-] couldn't save notification '{notification['id']}' :( \n")
        pass
    return 0



def Retrive_Notification_From_Db(notification):
    """

    :param notification: collection name
    :return: list of
    """
    # Connection to Database in specific collection "entities"
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    collection_notifications = db[notification]
    return list(collection_notifications.find())

# function for saving entities (JSON File) into "entities" collection in MongoDB Database
def Save_Subscriptoin_To_Db(subscription):
    # Connection to Database in specific collection "entities"
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    collection_entities = db['subscriptions']
    return collection_entities.save(subscription)


def update_service(notification):
    # Connection to Database in specific collection "entities"
    try:
        print('\n saving notification .................\n')
        db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
        collection_notifications = db["services"]
        collection_notifications.save(notification)
        print(f"\n[+] notification '{notification['id']}' saved successfully ^^\n")
    except:
        print(f"\n[-] couldn't save notification '{notification['id']}' :( \n")
        pass
    return 0
############## to Store Entity using Pymodm library  ######################

# connect('mongodb://{}:{}/{}'.format(DBhost, DBport, DBname))
#
# class Entities(MongoModel):
#     # Entity 'id' as the '_id' field in MongoDB.
#     id = fields.CharField(primary_key=True)
#     #entitiy_id = fields.CharField(primary_key=True)
#     attributes = fields.DictField()
#     #temperature = fields.IntegerField()
#     #pH = fields.IntegerField()
#
# class User(MongoModel):
#     # Use 'email' as the '_id' field in MongoDB.
#     email = fields.EmailField(primary_key=True)

