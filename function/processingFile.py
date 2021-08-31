import shutil
import datetime
import os
import pandas as pd
import pyodbc

pathLog = r"C:\Users\HPDQ\tranfer-file-2\data\log.txt"
pathSourceFile = r"C:\Users\HPDQ\tranfer-file-to-another-PC\data\Gang_kipA-2208.csv"
pathDesFile = r"C:\Users\HPDQ\tranfer-file-2\data\done"

def writeLog(log):
    with open(pathLog, 'a') as f:
            f.write("\n")
            f.write(str(datetime.datetime.now()))
            f.write(log)
            
def readFile(file):
    df = pd.read_csv(file)
    return df

def moveFile(pathSourceFile, PathDesFile):

    timeNow = datetime.datetime.now()
    fileName = ""
    fileName = str(timeNow.year) + str(timeNow.month) + str(timeNow.day) + "_"+ str(timeNow.hour) + str(timeNow.minute) + str(timeNow.second)
    PathDesFile = os.path.join(PathDesFile, fileName + ".csv")
    log = pathSourceFile + "->" + PathDesFile
    #print (log)
    #print (pathDesFile)
    writeLog(log)
    shutil.move(pathSourceFile, PathDesFile)

def connectDatabase(server, database, username, password):
    '''server = 'localhost\SQLEXPRESS' 
    database = 'NMLGANG_DB' 
    username = 'sa' 
    password = '123456' 
    kiểm tra driver có phù hợp hay không?'''
    connStr = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=localhost\SQLEXPRESS;'
                            'Database=NMLGANG_DB;'
                            'Trusted_Connection=yes;')
    #connStr = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = connStr.cursor()
    return connStr, cursor

def insertThongSoMeDatabase(connStr, cursor, df):
    for index,row in df.iterrows():
        cursor.execute("INSERT INTO NMLGANG_DB.dbo.NMLGANGTABLE_THONGSOME (ID, thoiGian, caID, meGang, soThung, sanRaGang) VALUES(?,?,?,?,?,?)", row['ten'], row['date'], row['Ca'], row['mẻ Gang'],  row['số thùng'], row['sàn ra Gang'])
        connStr.commit()
    #cursor.close()
    #connStr.close()

def insertThongSoVatLyDatabase(connStr, cursor, df):
    for index,row in df.iterrows():
        cursor.execute("INSERT INTO NMLGANG_DB.dbo.NMLGANGTABLE_THONGSOVATLYME (ID, thoiGianRaGang, gianCach, thoiGianRaXi, tiLeTGGangXi, doSauLoGang, luongBunBit, sanLuong, nhietDoGang, khoiLuong, loaiGang) VALUES(?,?,?,?,?,?,?,?,?,?,?)", row['ten'], row['thời Gian Ra Gang'],row['giản Cách'], row['thời Gian Ra Xỉ'],row['Thời Gian Ra Xỉ trên Ra Gang'], row['độ Sâu Lỗ Gang'],row['lượng Bùn Bịt'], row['sản Lượng Gang'],row['nhiệt độ Gang'], row['khối lượng'],row['loại Gang'])
        connStr.commit()
    #cursor.close()
    #connStr.close()

def insertThongSoHoaHocDatabase(connStr, cursor, df):
    for index,row in df.iterrows():
        cursor.execute("INSERT INTO NMLGANG_DB.dbo.NMLGANGTABLE_THONGSOHOAHOCME (ID, TPHH_C, TPHH_Si, TPHH_Mn, TPHH_S, TPHH_P, TPHH_Ti, TPHH_SiO2, TPHH_Al2O3, TPHH_CaO, TPHH_MgO, TPHH_TiO2, TPHH_Ri) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", row['ten'], row['Thành phần hóa học C'], row['Thành phần hóa học Si'], row['Thành phần hóa học Mn'], row['Thành phần hóa học S'], row['Thành phần hóa học P'], row['Thành phần hóa học Ti'], row['Thành phần hóa học SiO2'], row['Thành phần hóa học Al2O3'], row['Thành phần hóa học CaO'], row['Thành phần hóa học MgO'], row['Thành phần hóa học TiO2'], row['Thành phần hóa học Ri'])
        connStr.commit()
    #cursor.close()
    #connStr.close()
def disconnected(connStr, cursor):
    cursor.close()
    connStr.close()
    
if __name__ == "__main__":
    print (readFile(pathSourceFile))
    #moveFile(pathSourceFile, pathDesFile)
