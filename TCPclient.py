import socket
import string
import random

kirim = "Give me access"
coun = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
s.send(kirim.encode())

txt = ''
txt2 = ''
while True:
	key_rev = s.recv(1024)
	key_rev = key_rev.decode()
	if key_rev == 'this is your key':
		for i in range (5):
			coun = coun + 1
			# print(coun)
			data = s.recv(1024)
			data = data.decode()
			txt = txt + data
	if coun == 5:
		for i in range (5):
			lower_alphabet = string.ascii_lowercase
			random_letter = random.choice(lower_alphabet)
			s.send(random_letter.encode())
			txt2 = txt2 + random_letter
			#print(random_letter)
		break

s.close()
print("Send to Server : " + txt2)
print("ini Karcis anda : " + txt)