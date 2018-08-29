# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re

def parse_cfg(fname):
    f = open(fname)
    rslt = {}
    z = ''
    for each in f:
        xmatch = re.search('address \d+.\d+.\d+.\d+ \d+.\d+.\d+.\d+ secondary', each)
        zmatch = re.search('address \d+.\d+.\d+.\d+ \d+.\d+.\d+.\d+', each)
        t = re.search('interface \w+\d+/\d+|interface \w+\d+', each)
        if t:
            z = t.group()
            continue
        elif zmatch:
            if xmatch:
                xmatch = xmatch.group()
                ip_addr = xmatch.split(' ')[1]
                netmask = xmatch.split(' ')[2]
                tmp_list2 = [ip_addr, netmask]
                tmp_list3 = tuple(tmp_list1+tmp_list2)
                #my_list = tuple(tmp_list3)
                rslt[z] = tmp_list3
            else:
                zmatch = zmatch.group()
                ip_addr = zmatch.split(' ')[1]
                netmask = zmatch.split(' ')[2]
                tmp_list1 = [ip_addr, netmask]
                tmp_list = tuple(tmp_list1)
                #rslt.append(tmp_list)
                rslt[z] = tmp_list
        else:
            continue
    print(rslt)

parse_cfg('config_r2.txt')
