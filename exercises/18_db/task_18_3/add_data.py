# -*- coding: utf-8 -*-
'''
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding, но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''

import glob
import re
import sqlite3
import yaml

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print(dhcp_snoop_files)

def add_data_snooping():
    rslt = []
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()
    for each in dhcp_snoop_files:
        with open(each) as zzz:
            for line_search in zzz:
                search_pattern = '([A-F0-9]{2}:[A-F0-9]{2}:[A-F0-9]{2}:[A-F0-9]{2}:[A-F0-9]{2}:[A-F0-9]{2})\s+(\S+)\s+\d+\s+\S+\s+(\d+)\s+(\S+)'
                regex = re.search(search_pattern, line_search)
                switch_name = re.search('sw\d+', each)
                if regex and switch_name:
                    tmp = []
                    tmp = [regex.group(1), regex.group(2), regex.group(3), regex.group(4), switch_name.group(), '1']
                    set_active_query = 'UPDATE dhcp set active = 0 WHERE switch = \'{}\''.format(switch_name.group())
                    print(set_active_query)
                    cursor.execute(set_active_query)
                    connection.commit()
                    rslt.append(tmp)
    #print(rslt)
    cursor.executemany('INSERT INTO dhcp VALUES (?,?,?,?,?,?)', rslt)
    connection.commit()

def add_data_switches():
    with open('switches.yml') as yaml_list:
        zhopa = yaml.load(yaml_list)
        dict_to_convert = list(zhopa['switches'].items())
        print(dict_to_convert) 
        connection = sqlite3.connect(db_filename)
        cursor = connection.cursor()
        cursor.executemany('INSERT INTO switches VALUES (?,?)', dict_to_convert)
        connection.commit()


#add_data_switches()

add_data_snooping()
