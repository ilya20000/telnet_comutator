#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# получить Хосты и их ip из zabbix

from pyzabbix import ZabbixAPI
#import json

def getHosts(mag):
    if len(mag) < 1:
        print("Нет параметра -m")
        exit()

    #Пробуем подключиться к заббиксу
    try:
        zabbixApi = ZabbixAPI("http://192.168.1.202")
        zabbixApi.login("tasker", "reksat")
    except Exception as e:
        print("Can't connect to zabbix server %s" % str(e))
        exit()
    # получаем список айпи адресов
    apHostsFromzabbix = zabbixApi.host.get(
        search={"name": mag+"-sw"},
        filter={"status":"0"},
        #output=['host', 'name'],
        monitored_hosts=True,
    )
    listComutators = []
    print(apHostsFromzabbix)
    for item in apHostsFromzabbix:
        listComutators.append(item["host"])

    # записываем в файл
    #with open('ipSw.json', 'w') as f:
    #    json.dump(apHostsFromzabbix, f, ensure_ascii=False)
    return listComutators

if __name__ == '__main__':
    getHosts('m2')