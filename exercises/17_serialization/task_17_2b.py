# -*- coding: utf-8 -*-
'''
Задание 17.2b

Переделать функциональность скрипта из задания 17.2a,
в функцию generate_topology_from_cdp.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_file - этот параметр управляет тем, будет ли записан в файл, итоговый словарь
 * значение по умолчанию - True
* topology_filename - имя файла, в который сохранится топология.
 * по умолчанию, должно использоваться имя topology.yaml.
 * топология сохраняется только, если аргумент save_to_file указан равным True

Функция возвращает словарь, который описывает топологию.
Словарь должен быть в том же формате, что и в задании 17.2a.

Проверить работу функции generate_topology_from_cdp на файлах:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Записать полученный словарь в файл topology.yaml.

Не копировать код функции parse_sh_cdp_neighbors
'''

import re
import glob
import yaml

def generate_topology_from_cdp(list_of_files, save_to_file=True, topology_filename='topology.yaml'):
    
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
    
    zaloopa = []

    for filez in list_of_files:
        with open(filez) as f:
            pizda = f.readlines()
            xyz = parse_sh_cdp_neighbors(pizda)
            zaloopa.append(xyz)
    
    if save_to_file:
        with open(topology_filename, 'w') as xyz:
            yaml.dump(zaloopa, xyz)


list_of_files = glob.glob('sh_cdp_n_*')

generate_topology_from_cdp(list_of_files, save_to_file=True, topology_filename='topology.yaml')
