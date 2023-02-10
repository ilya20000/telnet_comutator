#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telnetlib import Telnet
from time import sleep

import sys
import argparse
     
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-m', '--mag', nargs='?')
    parser.add_argument ('-a', '--adduser', nargs='?')
    parser.add_argument ('-d', '--deluser', nargs='?')
    parser.add_argument ('-p', '--pass', nargs='?')
    parser.add_argument ('-r', '--rights', nargs='?')
    return parser


def whatToDo(arguments):
    if arguments.adduser != None :
        return 'adduser'
    elif arguments.deluser != None :
        return 'deluser'


def doOperation(arguments):
    operation = whatToDo(arguments) #Какую операцию нужно выполнить? Добавление-удаление.
    if operation == 'adduser':
        addUser(arguments)

def addUser():
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


if __name__ == '__main__':
    parser = createParser()
    arguments = parser.parse_args(sys.argv[1:])
    doOperation(arguments)
    print ("Привет, {}!".format (namespace.mag) )



exit()
user = 'admin'
password = '123'
timeout = 5
try:
    tn = Telnet('10.2.2.4', 23, timeout)
except Exception as e:
    print("error: %s " % str(e))
    if str(e) == "timed out":
        print("connect via ssh")


