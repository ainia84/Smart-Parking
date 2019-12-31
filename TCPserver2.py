import socket
import string
import random
from time import sleep
#from pymongo import MongoClient
import mysql.connector

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(('localhost', 50000))
print ("Ready")
coun = 0
count = 0
masuk = 0
hasil1 = ""
hasil2 = ""
hasil3 = ""
key = "this is your key"

#try: 
#    sambung = MongoClient('mongodb://alif:alif@cluster0-6a9pu.mongodb.net/test',27017) 
#    print("Connected successfully!!!") 
#except:   
#    print("Could not connect to MongoDB") 
while True:
    if coun == 0:
        plat = ''
        plat2 = ''
        hasil1 = ""
        hasil2 = ""
        hasil3 = ""

        s.listen()
        conn, addr = s.accept()
        data = conn.recv(1024)
        data = data.decode()
        if data == 'Give me access':
            masuk = masuk + 1
            print(masuk)
            conn.send(key.encode())
            sleep(1)
            for i in range (5):
                upper_alphabet = string.ascii_uppercase
                random_letter = random.choice(upper_alphabet)
                conn.send(random_letter.encode())
                # print(random_letter)
                coun = coun + 1
                # print(coun)
                plat2 = plat2 + random_letter
                sleep(1)
        if coun == 5:
            for i in range (5):
                plat_buff = conn.recv(1024)
                plat_buff = plat_buff.decode()
                plat = plat + plat_buff
                count = count + 1
        if count == 5:
            print("Karcis client : " + plat2)
            print ("Plat client : " + plat)

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Ainiaalif123",
                database="parkir")

            hasil1 = plat2
            hasil2 = plat
            hasil3 = masuk  

            mycursor = mydb.cursor()

            sql = "INSERT INTO smartp (Karcis,plat,masuk) VALUES (%s,%s,%s)"
            mycursor.execute(sql, (hasil1,hasil2,hasil3))

            mydb.commit()

            coun = 0
            count = 0
    
conn.close()


#db = sambung.SmartParking
#collection = db.Smart_Parking

#emp_rec1 = { 
#        "name":"Mr.Geek", 
#        "eid":24, 
#        "location":"delhi"
#        } 

#isi = collection.insert_one(emp_rec1)
#isi2 = collection.insert_one(plat2)
