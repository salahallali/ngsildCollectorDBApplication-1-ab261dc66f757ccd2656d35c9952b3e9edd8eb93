from pymongo import MongoClient


#function returns a connection to a Database
def Db_Connect(DBhost, DBport, DBname):
    client = MongoClient('{}'.format(DBhost), int(DBport))
    db = client['{}'.format(DBname)]
    return db