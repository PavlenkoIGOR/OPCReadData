from multiprocessing import connection
from sqlite3 import Cursor
from uu import decode
from Models.ORG_DTO import ORG_DTO
from Services.ConnectionMaker import ConnectionMaker
from Repository.EntitiesRepo import EntitiesRepo

    

    
# def ConnectToDB():
#     connectionMaker = ConnectionMaker()
#     my_connection = connectionMaker.MakeConnection()
#     if my_connection:
#         print("connection established! :) ")
                
#         # ���������� ����������� �������� ��� �������
#         with my_connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM \"Organizations\"")  # ��������� ������
#             results = cursor.fetchall()  # ��������� ��� ����������
            
#             # ������� ���������� � �������
#             for row in results:
#                 print(row)  # �������� ������ ������ ����������
#         my_connection.cursor().close()
#     else:
#         print("connection not established! :(")


def GetEntities():
    connectionMaker = ConnectionMaker()
    enttitiesRepo = EntitiesRepo(connectionMaker)
    organizations = []
    organizations = enttitiesRepo.GetOrganizations()
    for org in organizations:
        print(f"Organization: {org}")
    


def main():
    # ConnectToDB()
    GetEntities()
    
    
if __name__ == "__main__":
    main()
    