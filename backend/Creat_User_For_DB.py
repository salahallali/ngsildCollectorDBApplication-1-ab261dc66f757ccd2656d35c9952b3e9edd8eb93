
# function for creating users in MongoDB Database

from backend.Connection_To_Db import Db_Connect
from backend.LoadConfigFile_and_Parameters import DBhost, DBport, DBname, DBuser, DBpwd


def Create_User_For_Db(username, password, allowed_to_update):
    # Connection to Database
    db = Db_Connect(DBhost, DBport, DBname, DBuser, DBpwd)
    if allowed_to_update:
        return db.add_user(f'{username}', f'{password}', roles=[{'role': 'readWrite', 'db': 'NGSI_LDCollector_DB'}])
    else:
        return db.add_user(f'{username}', f'{password}', roles=[{'role': 'read', 'db': 'NGSI_LDCollector_DB'}])