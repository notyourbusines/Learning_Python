# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config_file):
    
    f = open(config_file, 'r')
    
    sort_lst = []
    tmp_sort_list =()
    for each in f:
        if 'interface FastEthernet' in each or 'access vlan' in each or 'allowed vlan' in each or 'mode access' in each:
            each = each.strip("\n")
            each = each.strip(" ")
            sort_lst.append(each)
    
    print(sort_lst)
    
    access_dict = {}
    trunk_dict = {}

    for i in range(len(sort_lst)):
        if sort_lst[i].startswith('interface'):
            if (i+2) > len(sort_lst)-1:
                print('Программа завершена!')
                break
            elif sort_lst[i+1].endswith('mode access'):
                if sort_lst[i+2].startswith('switchport access'):
                    access_dict[sort_lst[i].split()[1]] = sort_lst[i+2].split()[3]
                    print(access_dict)
                else:
                    access_dict[sort_lst[i].split()[1]] = '1'
                    print(access_dict)
            elif sort_lst[i+1].startswith('switchport trunk'):
                trunk_dict[sort_lst[i].split()[1]] = sort_lst[i+1].split()[4]
                print(trunk_dict)
            else:
                print('Интерфейс без конфига!')
    
    
get_int_vlan_map('config_sw2.txt')
