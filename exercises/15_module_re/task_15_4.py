# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''
import re

def parse_sh_ip_int_br(fname):
    rslt = []
    xyz = []
    f = open(fname)
    for each in f:
        t = re.search('Ethernet|Loopback', each)
        if t:
            if t:
                infr, ipaddr, *other, stat, proto = each.split()
                tmp_lst = [infr, ipaddr, stat, proto]
                rslt.append(tuple(tmp_lst))
    print(rslt)

parse_sh_ip_int_br('sh_ip_int_br_2.txt')
