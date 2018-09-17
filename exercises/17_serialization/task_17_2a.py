# -*- coding: utf-8 -*-
'''
Задание 17.2a

С помощью функции parse_sh_cdp_neighbors из задания 17.2,
обработать вывод команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Объединить все словари, которые возвращает функция parse_sh_cdp_neighbors,
в один словарь topology и записать его содержимое в файл topology.yaml.

Структура словаря topology должна быть такой:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}},
 'R5': {'Fa0/1': {'R4': 'Fa0/1'}},
 'R6': {'Fa0/0': {'R4': 'Fa0/2'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Не копировать код функции parse_sh_cdp_neighbors
'''

import re
import glob
import yaml

def parse_sh_cdp_neighbors(output):
    rslt = {}
    for each in output:
        tmp = {}
        l_hname_parse = re.search('(\w+)(\>)', each)
        cdp_parse = re.search('(?P<r_hname>\S+)\s+(?P<l_intf>\S+\s+\d+/\d+).+(?P<r_intf>Eth \d+/\d+)', each)
        if l_hname_parse:
            l_hname = l_hname_parse.group(0)
            rslt[l_hname] = {}
        elif cdp_parse:
            r_hname = cdp_parse.group('r_hname')
            #print(r_hname)
            l_intf = cdp_parse.group('l_intf')
            #print(l_intf)
            r_intf = cdp_parse.group('r_intf')
            #print(r_intf)
            tmp[r_hname] = r_intf
            rslt[l_hname][l_intf] = tmp
    return(rslt)

sh_version_files = glob.glob('sh_cdp_n_*')

zaloopa = []

for filez in sh_version_files:
    with open(filez) as f:
        pizda = f.readlines()
        xyz = parse_sh_cdp_neighbors(pizda)
        zaloopa.append(xyz)

with open('topology.yaml', 'w') as xyz:
    yaml.dump(zaloopa, xyz)


