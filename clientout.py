import socket
import string
import random
from time import sleep
import mysql.connector

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.connect(('localhost', 5000))
coun = 0


while True:
    if coun == 0:
        karcis_in = input("Karcis : ")
        s.send(karcis_in.encode())
        sleep(1)
        plat_in = input("Plat : ")
        s.send(plat_in.encode())
        sleep(1)
        coun = coun + 1
        permission = s.recv(1024)
        permission = permission.decode()
        coun = coun + 1
        if permission == 'Terima kasih':
            print("Terima kasih")
            coun = 0    
        else :
            print("Maaf karcis dan plat tidak cocok")
            coun = 0
            
            