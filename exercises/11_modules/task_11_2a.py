# -*- coding: utf-8 -*-
'''
Задание 11.2a

С помощью функции parse_cdp_neighbors из задания 11.1
и функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует выводу
команды sh cdp neighbor из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt


Не копировать код функций parse_cdp_neighbors и draw_topology.

В итоге, должен быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
import draw_network_graph as bbb
import parse_cdp_neighbors as fff

zzz1 = fff.parse_cdp_neighbors('sh_cdp_n_sw1.txt')
zzz2 = fff.parse_cdp_neighbors('sh_cdp_n_r1.txt')
zzz3 = fff.parse_cdp_neighbors('sh_cdp_n_r2.txt')
zzz4 = fff.parse_cdp_neighbors('sh_cdp_n_r3.txt')

zzz = {**zzz1,**zzz2, **zzz3, **zzz4}
print('Исходный массив:', zzz)

list2 = list(zzz.values())

print(list2)

p = zzz.copy()

for each in zzz:
    for zaloopa in list2:
        if each == zaloopa:
            del(p[each])
            list2.remove(zzz[each])
            break
       
print(p)
bbb.draw_topology(p, '/home/python/Learning_Python/exercises/11_modules/topology_11_2a_red')
