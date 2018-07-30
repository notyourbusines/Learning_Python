# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(file_name):
    f = open(file_name)
    
    result_dic = {}
    
    for each in f:
        if '>' in each:
            current_hostname = each.split('>')[0]
        elif 'Eth' in each.split():
            rmt_list = ()
            local_list = ()
            z = each.split()
            rmt_host, loc_intf, loc_num, *pizda, rmt_intf, rmt_num = z
            local_list = (current_hostname, loc_intf+loc_num)
            rmt_list = (rmt_host, rmt_intf+rmt_num)
            result_dic[local_list] = rmt_list
    return result_dic
        

xyz = parse_cdp_neighbors('sw1_sh_cdp_neighbors.txt')

print(xyz)
