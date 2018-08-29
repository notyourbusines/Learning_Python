# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re

def parse_cfg(fname):
    f = open(fname)
    rslt = {}
    z = ''
    for each in f:
        zmatch = re.search('address \d+.\d+.\d+.\d+ \d+.\d+.\d+.\d+', each)
        t = re.search('interface \w+\d+/\d+|interface \w+\d+', each)
        if t:
            z = t.group()
            continue
        elif zmatch:
            zmatch = zmatch.group()
            ip_addr = zmatch.split(' ')[1]
            netmask = zmatch.split(' ')[2]
            tmp_list = tuple([ip_addr, netmask])
            #rslt.append(tmp_list)
            rslt[z] = tmp_list
        else:
            continue
    print(rslt)

parse_cfg('config_r1.txt')
