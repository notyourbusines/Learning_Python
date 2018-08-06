# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess

def check_ip_addresses(ip_list):
    reachable_list = []
    unreachable_list = []
    
    for each in ip_list:
        result = subprocess.run(['ping', '-c', '3', '-n', each])
        if result.returncode == 0:
            reachable_list.append(each)
        else:
            unreachable_list.append(each)
            
    print(reachable_list)
    print(unreachable_list)


list_of_ips = ('8.8.8.8', '192.1.1.1')
#list_of_ips = ('8.8.8.8')

check_ip_addresses(list_of_ips)
    
