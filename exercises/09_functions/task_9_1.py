# -*- coding: utf-8 -*-
'''
Задание 9.1

Создать функцию, которая генерирует конфигурацию для access-портов.

Функция ожидает, как аргумент, словарь access-портов, вида:
    { 'FastEthernet0/12':10,
      'FastEthernet0/14':11,
      'FastEthernet0/16':17,
      'FastEthernet0/17':150 }

Функция должна возвращать список всех портов в режиме access
с конфигурацией на основе шаблона access_template.
Заготовка для функции уже сделана.

В конце строк в списке не должно быть символа перевода строки.

Пример итогового списка (перевод строки после каждого элемента сделан для удобства чтения):
[
'interface FastEthernet0/12',
'switchport mode access',
'switchport access vlan 10',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
'interface FastEthernet0/17',
'switchport mode access',
'switchport access vlan 150',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable',
...]

Проверить работу функции на примере словаря access_dict.


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
def generate_access_config(access):
2	    access_template = [
3	        'switchport mode access', 'switchport access vlan',
4	        'switchport nonegotiate', 'spanning-tree portfast',
5	        'spanning-tree bpduguard enable'
6	    ]
7	    
8	    for intf in access:
9	        print('interface ' + intf)
10	        for each in access_template:
11	            if each.endswith('access vlan'):
12	                print(each + ' ' + str(access[intf]))
13	            else: 
14	                print(each)
15	                
16	
17	
18	access_dict = {
19	    'FastEthernet0/12': 10,
20	    'FastEthernet0/14': 11,
21	    'FastEthernet0/16': 17,
22	    'FastEthernet0/17': 150
23	}
24	
25	generate_access_config(access_dict)
