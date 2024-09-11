import psycopg2
from Services.ConnectionData import host, port, user, password, database

class ConnectionMaker:
    
    def MakeConnection(self):
        try:
            connectionDB = psycopg2.connect(
                host = host,
                port = port,
                user = user,
                password = password,
                database = database
               )
            
            if connectionDB:
                return connectionDB
            
                 
            # with connectionDB.cursor() as psql_cursor: #аналог конструкции using()
            #     psql_cursor.execute("select * from \"Organizations\"")

        except Exception as ex:
            print(f"exception {ex}")
        # finally:
        #     if connectionDB:
        #         connectionDB.close()
        #         print("Connection closed")
    
    # def CloseConnection():
    #       if connectionDB:
    #             connectionDB.close()
    #             print("Connection closed")
         





