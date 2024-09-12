import psycopg2
from Services.ConnectionMaker import ConnectionMaker

class EntitiesRepo:
    
    def __init__(self, connectionMaker):
        self.connectionMaker = connectionMaker

    def GetOrganizations(self):
        
        connectionDB = self.connectionMaker.MakeConnection()
        organizations = []
        
        if connectionDB:
             with connectionDB.cursor() as cursor:
                  cursor.execute("select * from \"Organizations\"")
                  organizations = cursor.fetchall()
             connectionDB.close() #закрытие соединения
             return organizations
        else:
            return None




