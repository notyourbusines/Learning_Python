# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_file):
    
    f = open(config_file, 'r')
    
    sort_lst = []
    
    for each in f:
        if 'interface FastEthernet' in each or 'access vlan' in each or 'allowed vlan' in each:
            each = each.strip("\n")
            each = each.strip(" ")
            sort_lst.append(each)
                
    access_dict = {}
    trunk_dict = {}

    for i in range(len(sort_lst)):
        if sort_lst[i].startswith('interface'):
            if (i+1) > len(sort_lst)-1:
                print('Программа завершена!')
                break
            elif sort_lst[i+1].startswith('switchport access'):
                access_dict[sort_lst[i].split()[1]] = sort_lst[i+1].split()[3]
                print(access_dict)
            elif sort_lst[i+1].startswith('switchport trunk'):
                trunk_dict[sort_lst[i].split()[1]] = sort_lst[i+1].split()[4]
                print(trunk_dict)
            else:
                print('Интерфейс без конфига!')
    
    
get_int_vlan_map('config_sw1.txt')
