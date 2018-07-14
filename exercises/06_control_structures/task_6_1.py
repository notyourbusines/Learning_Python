# -*- coding: utf-8 -*-
'''
Задание 6.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip_address = input('Введите IP адрес в формате 10.0.1.1: ')

octet_A = ip_address.split('.')[0]
print(octet_A)

if '255.255.255.255' in ip_address:
        print('Ваш адрес LOCAL BROADCAST')
elif '0.0.0.0' in ip_address:
        print('Ваш адрес UNASSIGNED')    
elif int(octet_A) <= 127:
        print('Ваш адрес UNICAST класса A')
elif int(octet_A) > 127 and int(octet_A) <= 191:
        print('Ваш адрес UNICAST класса B')
elif int(octet_A) > 192 and int(octet_A) <= 223:
        print('Ваш адрес UNICAST класса C')
elif int(octet_A) > 223 and int(octet_A) <= 239:
        print('Ваш адрес MULTICAST класса D')
else:
     print('Ваш адрес UNUSED')
