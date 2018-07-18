# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
mac_template = '''{}      {}          {}'''

f = open('CAM_table.txt', 'r')
vlan_raw = []

for lines in f:
    lines = lines.split()
    if 'DYNAMIC' not in lines:
        continue
    else:
        vlan_raw.append(lines)
        #vlan, mac, learn, ports = lines
        #print(mac_template.format(vlan, mac, ports))

result = sorted(vlan_raw, key=lambda x: x[0])

for zaloopa in result:
    a,b,c,d = zaloopa
    print(mac_template.format(a, b, c, d))

f.close()

