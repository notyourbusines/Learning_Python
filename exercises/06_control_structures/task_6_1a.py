# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip_address = input('Введите IP адрес в формате 10.0.1.1: ')

octet_A = ip_address.split('.')[0]
octet_B = ip_address.split('.')[1]
octet_C = ip_address.split('.')[2]
octet_D = ip_address.split('.')[3]

if 0 <= int(octet_A) <= 255 and 0 <= int(octet_B) <= 255 and 0 <= int(octet_C) <= 255 and 0 <= int(octet_D) <= 255:
        print('Адрес верного формата')
else:
        print('Ваш адрес неверен')

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
