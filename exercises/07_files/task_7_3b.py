# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
mac_template = '''{}      {}          {}'''

in1 = input('Введите номер VLAN: ')

f = open('CAM_table.txt', 'r')
vlan_raw = []

for lines in f:
    lines = lines.split()
    if 'DYNAMIC' not in lines:
        continue
    else:
        vlan_raw.append(lines)

result = sorted(vlan_raw, key=lambda x: x[0])

for zaloopa in result:
    a,b,c,d = zaloopa
    if in1 not in a:
        continue
    else:
        print(mac_template.format(a, b, c, d))

f.close()
