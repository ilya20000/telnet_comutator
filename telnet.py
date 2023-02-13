#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telnetlib import Telnet
from time import sleep

import sys
import argparse
import getZabbixHost




def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-m', '--mag', nargs='?')
    parser.add_argument ('-a', '--adduser', nargs='?')
    parser.add_argument ('-d', '--deluser', nargs='?')
    parser.add_argument ('-p', '--passw', nargs='?')
    parser.add_argument ('-r', '--rights', nargs='?')
    return parser


def connectComutator(ipComutator):
    user = 'admin'
    password = '-'
    timeout = 5
    try:
        tn = Telnet(ipComutator, 23, timeout)
    except Exception as e:
        print("error: %s " % str(e))
        if str(e) == "timed out":
            print("connect via ssh")
    try:
        #tn.write(b"\n")
        print("Соединяемся с "+ipComutator)
        tn.read_until(b"UserName:",5)
        tn.write(user.encode('ascii') + b"\n")
        #sleep(1)
        tn.read_until(b"PassWord:",5)
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"\n")
        #sleep(1)
        tn.read_until(b"admin#",5)
        print(str(tn.read_very_eager(), 'utf-8'))
        return tn  
    except Exception as e:
        print("error: %s " % str(e))
        if str(e) == "timed out":
            print("connect via ssh")
        return False




def addUser(tn, arguments):
    #tn.write(b"show account\n")
    #print(tn.read_very_eager())
    #com = "create account "+ arguments.rights +" "+ arguments.adduser +" encrypt sha_1 "+ arguments.passw +"\n"
    com = "create account "+ arguments.rights +" "+ arguments.adduser +" encrypt plain_text "+ arguments.passw +"\n"
    tn.write( bytes(com, encoding='utf-8') )
    sleep(1)
    s = str(tn.read_very_eager(), 'utf-8')
    if s.find('Success') == -1:
        print(s)
    tn.write(b"logout\n")
    sleep(1)
    #print(str(tn.read_very_eager(), 'utf-8'))


def deluser(tn, arguments):
    print("del")

def getMagComutators(mag):
    print("Получаем список ip комутаторов на магазине №"+ mag)
    return getZabbixHost.getHosts(mag)



if __name__ == '__main__':
    parser = createParser()
    arguments = parser.parse_args(sys.argv[1:])

    listComutators = getMagComutators(arguments.mag)
    for ipComutator in listComutators:
        
        tn = connectComutator(ipComutator)
        if tn == False:
            exit()

        if arguments.adduser != None :
            addUser(tn, arguments)
        elif arguments.deluser != None :
            deluser(tn, arguments)
        tn.close()
    exit()