

# import pymodm
# from pymodm import connect, fields, MongoModel, EmbeddedMongoModel
# from pymongo import MongoClient






# function for saving subscriptions (JSON File) into "subscriptions" collection in MongoDB Database
import json

from backend.Connection_To_Db import Db_Connect
from backend.LoadConfigFile_and_Parameters import DBhost, DBport, DBname, DBpwd, DBuser


def Save_subscription_To_Db(subscription):
    # Connection to Database in specific collection "subscriptions"
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    collection_subscriptions = db['subscriptions']
    if type(subscription) is list:
        for subscription_i in subscription:
            #setting subscription ID in the Response file to "_id" instead of "id" to avoid redandency in the Database
            subscription_i['_id'] = subscription_i.pop('id')
            collection_subscriptions.save(subscription_i)
            subscription_i['id'] = subscription_i.pop('_id')
    else:
        subscription['_id'] = subscription.pop('id')
        collection_subscriptions.save(subscription)
        subscription['id'] = subscription.pop('_id')
    return 0


def Delete_subscription_from_Db(id,filter):
    # Connection to Database in specific collection "subscriptions"
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    collection_subscriptions = db['subscriptions']
    if filter == 'type':
        return collection_subscriptions.delete_many({'type': id})
    else:
        return collection_subscriptions.delete_one({'_id': id})



def Update_subscription_On_Db(subscription):
    # Connection to Database in specific collection "subscriptions"
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    collection_subscriptions = db['subscriptions']
    #setting subscription ID in the Response file to "_id" instead of "id" to avoid redandency in the Database
    subscription['_id'] = subscription.pop('id')
    collection_subscriptions.update({'_id':subscription['_id']}, {"$set": subscription}, upsert=False)
    subscription['id'] = subscription.pop('_id')
    return 0

def Save_Notification_To_Db(notification):
    # Connection to Database in specific collection "subscriptions"
    try:
        print('\n saving notification .................\n')
        db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
        collection_notifications = db['notifications']
        collection_notifications.save(notification)
        Update_subscription_On_Db(notification['data'][0])
        print(f"\n[+] notification '{notification['id']}' saved successfully ^^\n")
    except:
        print(f"\n[-] couldn't save notification '{notification['id']}' :( \n")
        pass
    return 0



def Retrive_Notification_From_Db(notification):
    # Connection to Database in specific collection "subscriptions"
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    collection_notifications = db['notifications']
    notifications = {}
    i = 0
    for x in collection_notifications.find():
        notifications[i] = x
        print(x)
        i = i + 1
    print(notifications)
    return notifications

# function for saving subscriptions (JSON File) into "subscriptions" collection in MongoDB Database
def Save_Subscriptoin_To_Db(subscription):
    # Connection to Database in specific collection "subscriptions"
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    collection_subscriptions = db['subscriptions']
    return collection_subscriptions.save(subscription)
############## to Store subscription using Pymodm library  ######################

# connect('mongodb://{}:{}/{}'.format(DBhost, DBport, DBname))
#
# class subscriptions(MongoModel):
#     # subscription 'id' as the '_id' field in MongoDB.
#     id = fields.CharField(primary_key=True)
#     #entitiy_id = fields.CharField(primary_key=True)
#     attributes = fields.DictField()
#     #temperature = fields.IntegerField()
#     #pH = fields.IntegerField()
#
# class User(MongoModel):
#     # Use 'email' as the '_id' field in MongoDB.
#     email = fields.EmailField(primary_key=True)
