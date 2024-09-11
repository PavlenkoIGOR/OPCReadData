from multiprocessing import connection
from sqlite3 import Cursor
from uu import decode
from Person import Person  # ����������� ����� Person �� ����� Person
from Employee import Employee  # ����������� ����� Person �� ����� Person
from Models.ORG_DTO import ORG_DTO
from Services.ConnectionMaker import ConnectionMaker

    

    
def ConnectToDB():
    connectionMaker = ConnectionMaker()
    my_connection = connectionMaker.MakeConnection()
    if my_connection:
        print("connection established! :) ")
                
        # ���������� ����������� �������� ��� �������
        with my_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM \"Organizations\"")  # ��������� ������
            results = cursor.fetchall()  # ��������� ��� ����������
            
            # ������� ���������� � �������
            for row in results:
                print(row)  # �������� ������ ������ ����������
        my_connection.cursor().close()
    else:
        print("connection not established! :(")

def main():
    ConnectToDB()
    
    
if __name__ == "__main__":
    main()
    