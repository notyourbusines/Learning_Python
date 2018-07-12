# -*- coding: utf-8 -*-
'''
Задание 5.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


user_input = input('Введите IP-сеть (в формате: 10.1.1.0/24): ')
user_input = user_input.split('.')
user_subnet = user_input[0:3]
octet_A, octet_B, octet_C = user_subnet
user_mask = (str(user_input[3]).split('/'))[-1]
ip_template_A = '''
Network:
{}       {}       {}       {}'''
print(ip_template_A.format(octet_A, octet_B, octet_C, '0'))
ip_template_B = '''
{:08b}       {:08b}       {:08b}       {:08b}'''
print(ip_template_B.format(int(octet_A), int(octet_B), int(octet_C), 0))
