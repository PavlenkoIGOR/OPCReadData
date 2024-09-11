import psycopg2
from Services.ConnectionMaker import ConnectionMaker

class OPCRepo:
    
    def MakeConnection():
        connectionMaker = ConnectionMaker()
        connectionMaker.MakeConnection()

    def GetOrganization():
        return 0




