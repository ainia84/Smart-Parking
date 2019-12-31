import socket
import string
import random
from time import sleep
import mysql.connector
from lib.sql import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(('localhost', 5000))
print ("Ready")
s.listen()
conn, addr = s.accept()
coun = 0
keluar = 0
hasil1 = ""
ty = 'Terima kasih'
sry = 'maaf'


while True:
	if coun == 0:
		print("Masukan karcis dan Plat")
		karcis_in = conn.recv(1024)
		karcis_in = karcis_in.decode()
		print("karcis : " + (karcis_in))
		plat_in = conn.recv(1024)
		plat_in = plat_in.decode()
		print("plat : " + plat_in)
		coun = coun + 1
		sleep(2)

		mydb = db("localhost", "root","Ainiaalif123","parkir")
		#engkuk ngeget data e teko msql dideleh nisor kene mik


		if plat_in == plat_in: #terus iki diganti,jika karcis karo plat sing diinputno cocok karo sing diget
			keluar = keluar + 1
			hasil1 = keluar

			key = "plat = \"{}\" AND karcis = \"{}\""
			key = key.format(plat_in, karcis_in)

			data = mydb.findCol("plat","smartp", key, False)
			
			if data == None:
				conn.send(sry.encode())
				print("Maaf karcis dan plat tidak cocok")
				coun = 0

			else:
				setValue = "Keluar = {}"
				setValue = setValue.format(keluar)
				key = "plat = \"{}\""
				key = key.format(plat_in)
				mydb.update("smartp", setValue, key)

				print(keluar)
				conn.send(ty.encode())
				print("Terima kasih")
				coun = 0

conn.close()