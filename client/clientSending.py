import socket
import os
file = r"C:\Users\HPDQ\data.csv"
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
    return 1
while True:
    print (client_speaking(file))