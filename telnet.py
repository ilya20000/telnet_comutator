#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telnetlib import Telnet
from time import sleep


user = 'admin'
password = '123'
timeout = 5


try:
    tn = Telnet('10.2.2.4', 23, timeout)
except Exception as e:
    print("error: %s " % str(e))
    if str(e) == "timed out":
        print("connect via ssh")

#tn.write(b"\n")
tn.read_until(b"UserName:",5)
tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"PassWord:",5)
tn.write(password.encode('ascii') + b"\n")
tn.write(b"\n")
tn.read_until(b"admin#",5)


#tn.write(b"show account\n")
tn.write(b"create account operator test123 encrypt sha_1 7868dd04d3a9e04ace1c6c8c6af1c05202d5c154\n")
print(tn.read_very_eager())
sleep(2)
#print(tn.read_very_eager())
tn.write(b"logout\n")
sleep(1)
#print(tn.read_very_eager())
tn.close()
