from pymongo import MongoClient

#function returns a connection to a Database
def Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd):

    client = MongoClient(f'mongodb://{DBuser}:{DBpwd}@{DBhost}:{DBport}/admin')
    db = client['{}'.format(DBname)]
    return db
