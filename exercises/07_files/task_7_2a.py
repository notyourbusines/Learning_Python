# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

d,a,c = ignore

print(type(d))

file_name = argv[1]

f = open(file_name, 'r')

for line in f:
    if '!' in line:
        continue
    elif d in line or a in line or c in line:
        continue
    else: 
        print(line.replace("\n", ""))
    
   
