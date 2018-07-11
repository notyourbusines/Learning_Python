# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес в двоичную строку (без двоеточий).

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'
MAC_list = MAC.replace(':','')
MAC_list_1 = MAC_list[0:2]
MAC_list_2 = MAC_list[2:4]
X1 = str(int(MAC_list_1, 16))
X2 = str(int(MAC_list_2, 16))
print(X1,X2)
result_x = str(X1 + X2)
print(result_x)
