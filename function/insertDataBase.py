from createDataFrame import create_dataframe
from processingFile import connectDatabase, disconnected, insertThongSoMeDatabase, insertThongSoVatLyDatabase, insertThongSoHoaHocDatabase
from datetime import datetime, time
import time

def insert_database(file):
    start = datetime.now()
    #file = r'C:\Users\HPDQ\tranfer-file-to-another-PC\data\Gang_test_ver2.csv'
    server = 'localhost\SQLEXPRESS'
    database = 'NMLGANG_DB' 
    username = 'sa' 
    password = '123456' 

    luyenGang_DF = create_dataframe(file)
    connStr, cursor = connectDatabase(server, database, username, password)
    insertThongSoMeDatabase(connStr, cursor, luyenGang_DF)
    time.sleep(1)
    #connStr, cursor = connectDatabase(server, database, username, password)
    insertThongSoVatLyDatabase(connStr, cursor, luyenGang_DF)
    #connStr, cursor = connectDatabase(server, database, username, password)
    insertThongSoHoaHocDatabase(connStr, cursor, luyenGang_DF)
    disconnected(connStr, cursor)
    print (datetime.now() - start)

def insert_database_with_rabbitMQ(luyenGang_DF):
    start = datetime.now()
    #file = r'C:\Users\HPDQ\tranfer-file-to-another-PC\data\Gang_test_ver2.csv'
    server = 'localhost\SQLEXPRESS'
    database = 'NMLGANG_DB' 
    username = 'sa' 
    password = '123456' 
    connStr, cursor = connectDatabase(server, database, username, password)
    insertThongSoMeDatabase(connStr, cursor, luyenGang_DF)
    time.sleep(1)
    #connStr, cursor = connectDatabase(server, database, username, password)
    insertThongSoVatLyDatabase(connStr, cursor, luyenGang_DF)
    #connStr, cursor = connectDatabase(server, database, username, password)
    insertThongSoHoaHocDatabase(connStr, cursor, luyenGang_DF)
    disconnected(connStr, cursor)
    print (datetime.now() - start)