import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='VeteraKTK',
                                         user='ktk-application',
                                         password='1DBqFw0yTCAvc5GYxZpL9jkR7lB273',port=1433)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("YEAH MOTHERFUCKER")


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
