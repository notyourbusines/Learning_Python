# -*- coding: utf-8 -*-
'''
Задание 9.1b

Сделать копию скрипта задания 9.1a.

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/12'
    - значения: список команд, который надо выполнить на этом интерфейсе:
                          ['switchport mode access',
                           'switchport access vlan 10',
                           'switchport nonegotiate',
                           'spanning-tree portfast',
                           'spanning-tree bpduguard enable']


Проверить работу функции на примере словаря access_dict,
с генерацией конфигурации port-security и без.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


def generate_access_config(access, ps = True):
    result_dic = {}
    result_list =[]
    
    access_template = [
        'switchport mode access', 'switchport access vlan',
        'switchport nonegotiate', 'spanning-tree portfast',
        'spanning-tree bpduguard enable'
    ]

    port_security = [
        'switchport port-security maximum 2',
        'switchport port-security violation restrict',
        'switchport port-security'
    ]
    for intf in access:
        result_list = []
        for each in access_template:
            if ps:
                if each.endswith('access vlan'):
                    st = each + ' ' + str(access[intf])
                    result_list.append(st)
                elif port_security[0] not in result_list:
                        for zaloopka in port_security:
                            result_list.append(zaloopka)
                        result_list.append(each)
                else:
                    result_list.append(each)
            elif ps == False:
                if each.endswith('access vlan'):
                    st = each + ' ' + str(access[intf])
                    result_list.append(st)                            
                elif ps == False:
                    result_list.append(each)                    
        result_dic[intf] = result_list
    print(result_dic)


access_dict = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17,
    'FastEthernet0/17': 150
}

generate_access_config(access_dict)
