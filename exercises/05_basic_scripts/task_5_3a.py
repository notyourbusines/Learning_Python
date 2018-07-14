# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = '''
    interface {}
    switchport mode access
    switchport access vlan {}
    switchport nonegotiate
    spanning-tree portfast
    spanning-tree bpduguard enable
'''

trunk_template = '''
    interface {} 
    switchport trunk encapsulation dot1q
    switchport mode trunk
    switchport trunk allowed vlan {}
'''

dict ={'access' : {'Interface': 'None', 'Vlan': 'None', 'Template': access_template, 'Question': 'Enter VLAN number: '}, 
'trunk' : {'Interface': 'None', 'Vlan': 'None', 'Template': trunk_template, 'Question': 'Enter Allowed VLANs: '}}
i1 = input('Enter interface mode (access/trunk): ')
i2 = input('Enter interface type and number: ')
i3 = input(dict[i1]['Question'])
dict[i1]['Interface'] = i2
dict[i1]['Vlan'] = i3
print((dict[i1]['Template'].format(dict[i1]['Interface'], dict[i1]['Vlan'])))
