# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

XYZ = (ospf_route.split())
XYZ[0] = 'OSPF'
XYZ[2] = XYZ[2].replace(']','').replace('[','')
XYZ[5] = XYZ[5].replace(',','')
XYZ[4] = XYZ[4].replace(',','')
print(XYZ)

zaloopa = '''

Protocol:              {d[0]}
Prefix:                {d[1]}
AD/Metric:             {d[2]}
Next-Hop:              {d[4]}
Last update:           {d[5]}
Outbound Interface:    {d[6]}

'''
print(zaloopa.format(d=XYZ))
