# -*- coding: utf-8 -*-
'''
Задание 18.2a

Дополнить скрипт get_data.py из задания 18.2

Теперь должна выполняться проверка не только по количеству аргументов,
но и по значению аргументов.
Если имя аргумента введено неправильно, надо вывести сообщение об ошибке
(пример сообщения ниже).

Файл БД можно скопировать из прошлых заданий

В итоге, вывод должен выглядеть так:

$ python get_data_ver1.py vln 10
Данный параметр не поддерживается.
Допустимые значения параметров: mac, ip, vlan, interface, switch

'''

import sqlite3
from sys import argv
from tabulate import tabulate

def connect_to_db():
    db_filename = 'dhcp_snooping.db'
    connection = sqlite3.connect(db_filename)
    return connection

if argv[1] not in {'mac', 'ip', 'vlan', 'interface', 'switch'}:
    print('This data pattern is not supported! ')
elif(len(argv) == 3):
    keyz, valuez = argv[1:]
    piska = connect_to_db()
    cursor = piska.cursor()
    cursor.execute('SELECT * from dhcp WHERE {} = "{}"'.format(keyz, valuez))
    rowz = cursor.fetchall()
    rslt = []
    tmp = []
    for each in rowz:
        #print(each)
        #tmp = []
        mac, vlan, _, intf, sw = each
        mac_mac = ['mac', mac]
        vlan_vlan = ['ip', vlan]
        intf_intf = ['interface', intf]
        sw_sw = ['sw', sw]
        tmp.append(tuple(mac_mac))
        tmp.append(tuple(vlan_vlan))
        tmp.append(tuple(intf_intf))
        tmp.append(tuple(sw_sw))
        print(tmp)
    print(tabulate(tmp))
elif (len(argv) == 1):
    piska = connect_to_db()
    cursor = piska.cursor()
    cursor.execute('SELECT * from dhcp')
    rowz = cursor.fetchall()
    print('Table DHCP contains following records: ')
    print((rowz))
    #print(tabulate(rowz))
else:
    print('User 0 or 2 arguments only!')
