# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)


def conf_file_handle(file_name):
    
    sort_list = []
    result_list = {}
        
    f = open(file_name, 'r')
    
    for each in f:
        if '!' in each:
            continue
        elif check_ignore(each, ignore):
            continue
        else:
            sort_list.append(each.strip("\n"))
        
    result_list = {}
        
    for zaloopa in sort_list:
        if not zaloopa.startswith(' '):
            t = zaloopa
            result_list[zaloopa] = '1'
            sort_level2 = {}
            sort_level3 = []
        elif zaloopa.startswith('  '):
            sort_level3.append(zaloopa)
            result_list[t][y] = sort_level3
        else:
            y = zaloopa
            sort_level2[zaloopa] = ''
            result_list[t] = sort_level2
    print(result_list)
    
conf_file_handle('config_r1.txt')
