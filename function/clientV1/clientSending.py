import socket
import os
import time
import shutil
import datetime

pathFile = r"D:\duLieuVanHanh\client\data"

def client_speaking(filename):

    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096
    host = "192.168.113.32"
    port = 5001
    filesize = os.path.getsize(filename)
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")
    print ("file name: ", filename)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode('utf-8'))
    with open(filename, "rb", encoding='utf-8') as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
    s.close()
    time.sleep(2)
    return 1

def moveFile(pathFile, pathSourceFile, moveTo):

    timeNow = datetime.datetime.now()
    fileName = ""
    fileName = str(timeNow.year) + str(timeNow.month) + str(timeNow.day) + "_"+ str(timeNow.hour) + str(timeNow.minute) + str(timeNow.second)
    #pathSourceFile = os.path.join(pathFile, "in",  "data.csv")
    if moveTo == 1:
        PathDesFile = os.path.join(pathFile, "done",fileName + ".csv")
    else:
        PathDesFile = os.path.join(pathFile, "failer",fileName + ".csv")
    print (pathSourceFile)
    print (PathDesFile)
    #shutil.move(pathSourceFile, PathDesFile)

def client_speak(fileName):
    try:
        moveTo = client_speaking(fileName)
    except:
        moveTo = -1
    moveFile(pathFile, fileName, moveTo)