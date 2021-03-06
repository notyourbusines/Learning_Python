# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

user_input = argv[1]
user_input_init = str((user_input.split('/'))[0])
user_input_mask = int(str((user_input.split('/'))[1]))
user_input_list = user_input_init.split('.')
print('Маска сети десятичная: ', user_input_mask)
octet_A, octet_B, octet_C, octet_D = user_input_list
mask_binary = user_input_mask*'1'+(32-user_input_mask)*'0'
print('Маска сети двоичная: ', mask_binary)
subnet_binary = "{0:08b}".format(int(octet_A)) + "{0:08b}".format(int(octet_B))+"{0:08b}".format(int(octet_C))+"{0:08b}".format(int(octet_D))
subnet_trimmed = subnet_binary[:(user_input_mask)]
subnet_full = subnet_trimmed + '0'*(32-user_input_mask)
print('Адрес сети в двоичной: ', subnet_full)
octet_A_mask = int(subnet_full[:8], 2)
octet_B_mask = int(subnet_full[8:16], 2)
octet_C_mask = int(subnet_full[16:24], 2)
octet_D_mask = int(subnet_full[24:], 2)
print('Первый октет сетки в десятичной: ', octet_A_mask)
print('Второй октет сетки в десятичной: ', octet_B_mask)
print('Третий октет сетки в десятичной: ', octet_C_mask)
print('Четвертый октет маски в десятичной: ', octet_D_mask)
ip_template_A = '''
Network:
{}       {}       {}       {}'''
print(ip_template_A.format(octet_A_mask, octet_B_mask, octet_C_mask, octet_D_mask))
ip_template_B = '''
{:08b}       {:08b}       {:08b}       {:08b}'''
print(ip_template_B.format((octet_A_mask), (octet_B_mask), (octet_C_mask), (octet_D_mask)))
