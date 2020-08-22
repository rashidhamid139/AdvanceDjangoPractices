import boto3
import mysql.connector
from mysql.connector import Error

# try:
#     connection = mysql.connector.connect(host='mysqldbinstance.cikd7eiivmkw.ap-south-1.rds.amazonaws.com', database='bank',user='rashid139', password='Anamoly1')
# except Exception as e:
#     print(e)


# print(connection.get_server_info())

# cursor = connection.cursor()
# cursor.execute("select database();")
# record = cursor.fetchone()
# print("Your selected database is: ", record)

class DatabaseContextManager:
    __CONNECTIONS__ = 0
    def __init__(self):
        self.conn = mysql.connector.connect(host='mysqldbinstance.cikd7eiivmkw.ap-south-1.rds.amazonaws.com', database='bank',user='rashid139', password='Anamoly1')
        self.__CONNECTIONS__ =+ 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            return 
        self.conn.close()


with DatabaseContextManager() as databaseConn:
    cursor = databaseConn.conn.cursor()
    cursor.execute("SELECT * from account;")
    record = cursor.fetchone()
    print(record)


