# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''

import re

def parse_sh_cdp_neighbors(output):
    rslt = {}
    for each in output:
        tmp = {}
        l_hname_parse = re.search('(\w+)(\>)', each)
        cdp_parse = re.search('(?P<r_hname>\S+)\s+(?P<l_intf>\S+\s+\d+/\d+)\s+\d+\s+\S+\s\S+\s+\S+\s+\d+\s+(?P<r_intf>\S+\s+\d+/\d+)', each)
        if l_hname_parse:
            l_hname = l_hname_parse.group(0)
            rslt[l_hname] = {}
        elif cdp_parse:
            r_hname = cdp_parse.group('r_hname')
            print(r_hname)
            l_intf = cdp_parse.group('l_intf')
            print(l_intf)
            r_intf = cdp_parse.group('r_intf')
            print(r_intf)
            tmp[r_hname] = r_intf
            rslt[l_hname][l_intf] = tmp
    print(rslt)

with open('sh_cdp_n_sw1.txt') as f:
    pizda = f.readlines()
    #print(pizda)
    
parse_sh_cdp_neighbors(pizda)
