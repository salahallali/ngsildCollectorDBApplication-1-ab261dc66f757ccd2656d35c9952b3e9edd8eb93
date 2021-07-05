from backend.NGSI_Interpreter.Connection_To_Db import Db_Connect
from backend.NGSI_Interpreter.LoadConfigFile_and_Parameters import DBhost, DBport, DBname
# import pymodm
# from pymodm import connect, fields, MongoModel, EmbeddedMongoModel
# from pymongo import MongoClient






# function for saving entities (JSON File) into "entities" collection in MongoDB Database
def Save_Entity_To_Db(entity):
    # Connection to Database in specific collection "entities"
    db = Db_Connect(DBhost, DBport, DBname)
    collection_entities = db['entities']
    return collection_entities.save(entity)



# function for saving entities (JSON File) into "entities" collection in MongoDB Database
def Save_Subscriptoin_To_Db(subscription):
    # Connection to Database in specific collection "entities"
    db = Db_Connect(DBhost, DBport, DBname)
    collection_entities = db['subscriptions']
    return collection_entities.save(subscription)
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

