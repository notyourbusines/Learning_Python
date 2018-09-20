# -*- coding: utf-8 -*-
'''
На основе файла get_data_ver1.py из раздела, создать скрипт get_data.py.

Код в скрипте должен быть разбит на функции. Какие именно функции и как разделить код, надо решить самостоятельно. Часть кода может быть глобальной.

В примере из раздела, скрипту передавались два аргумента:

key - имя столбца, по которому надо найти информацию
value - значение
Теперь необходимо расширить функциональность таким образом:

если скрипт был вызван без аргументов, вывести всё содержимое таблицы dhcp более компактно (как в примере ниже)
если скрипт был вызван с двумя аргументами, вывести информацию из таблицы dhcp, которая соответствует полю и значению
если скрипт был вызван с любым другим количеством аргументов, вывести сообщение, что скрипт поддерживает только два или ноль аргументов
Обработка некорректного ввода аргумента будет выполняться в следующем задании

Файл БД можно скопировать из прошлых заданий

В итоге, вывод должен выглядеть так:

$ python get_data.py

В таблице dhcp такие записи:
----------------------------------------------------------------------
00:09:BB:3D:D6:58  10.1.10.2         10    FastEthernet0/1      sw1
00:04:A3:3E:5B:69  10.1.5.2          5     FastEthernet0/10     sw1
00:05:B3:7E:9B:60  10.1.5.4          5     FastEthernet0/9      sw1
00:07:BC:3F:A6:50  10.1.10.6         10    FastEthernet0/3      sw1
00:09:BC:3F:A6:50  192.168.1.100     100   FastEthernet0/5      sw1
00:A9:BB:3D:D6:58  10.1.10.20        10    FastEthernet0/7      sw2
00:B4:A3:3E:5B:69  10.1.5.20         5     FastEthernet0/5      sw2
00:C5:B3:7E:9B:60  10.1.5.40         5     FastEthernet0/9      sw2
00:A9:BC:3F:A6:50  100.1.1.6         3     FastEthernet0/20     sw3

$ python get_data.py ip 10.1.10.2

Detailed information for host(s) with ip 10.1.10.2
----------------------------------------
mac         : 00:09:BB:3D:D6:58
vlan        : 10
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------


$ python get_data.py vlan 10

Detailed information for host(s) with vlan 10
----------------------------------------
mac         : 00:09:BB:3D:D6:58
ip          : 10.1.10.2
interface   : FastEthernet0/1
switch      : sw1
----------------------------------------
mac         : 00:07:BC:3F:A6:50
ip          : 10.1.10.6
interface   : FastEthernet0/3
switch      : sw1
----------------------------------------
mac         : 00:A9:BB:3D:D6:58
ip          : 10.1.10.20
interface   : FastEthernet0/7
switch      : sw2
----------------------------------------

$ python get_data.py vlan
Пожалуйста, введите два или ноль аргументов
'''

import sqlite3
from sys import argv
from tabulate import tabulate

def connect_to_db():
    db_filename = 'dhcp_snooping.db'
    connection = sqlite3.connect(db_filename)
    return connection

if (len(argv) == 3):
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
        vlan_vlan = ['vlan', vlan]
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


    
