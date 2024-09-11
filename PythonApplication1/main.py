from multiprocessing import connection
from sqlite3 import Cursor
from uu import decode
from Person import Person  # Импортируем класс Person из файла Person
from Employee import Employee  # Импортируем класс Person из файла Person
from Models.ORG_DTO import ORG_DTO
from Services.ConnectionMaker import ConnectionMaker

    

    
def ConnectToDB():
    connectionMaker = ConnectionMaker()
    my_connection = connectionMaker.MakeConnection()
    if my_connection:
        print("connection established! :) ")
                
        # Используем контекстный менеджер для курсора
        with my_connection.cursor() as cursor:
            cursor.execute("SELECT * FROM \"Organizations\"")  # Выполняем запрос
            results = cursor.fetchall()  # Извлекаем все результаты
            
            # Выводим результаты в консоль
            for row in results:
                print(row)  # Печатаем каждую строку результата
        my_connection.cursor().close()
    else:
        print("connection not established! :(")

def main():
    ConnectToDB()
    
    
if __name__ == "__main__":
    main()
    