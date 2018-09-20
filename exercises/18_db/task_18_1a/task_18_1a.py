# -*- coding: utf-8 -*-
'''
Задание 18.1a

Скопировать скрипт add_data.py из задания 18.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''


import glob
import re
import sqlite3
from sqlite3 import Error
import yaml

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
#print(dhcp_snoop_files)

def add_data_snooping():
    rslt = []
    for each in dhcp_snoop_files:
        with open(each) as zzz:
            for line_search in zzz:
                search_pattern = '([A-F0-9]{2}:[A-F0-9]{2}:[A-F0-9]{2}:[A-F0-9]{2}:[A-F0-9]{2}:[A-F0-9]{2})\s+(\S+)\s+\d+\s+\S+\s+(\d+)\s+(\S+)'
                regex = re.search(search_pattern, line_search)
                switch_name = re.search('sw\d+', each)
                if regex and switch_name:
                    tmp = []
                    tmp = [regex.group(1), regex.group(2), regex.group(3), regex.group(4), switch_name.group()]
                    rslt.append(tmp)
    try:
        connection = sqlite3.connect(db_filename)
        cursor = connection.cursor()
        cursor.executemany('INSERT INTO dhcp VALUES (?,?,?,?,?)', rslt)
        connection.commit()
    except Error as e:
        print(e)

def add_data_switches():
    with open('switches.yml') as yaml_list:
        zhopa = yaml.load(yaml_list)
        dict_to_convert = list(zhopa['switches'].items())
        try:
            connection = sqlite3.connect(db_filename)
            cursor = connection.cursor()
            cursor.executemany('INSERT INTO switches VALUES (?,?)', dict_to_convert)
            connection.commit()
        except Error as e:
            print(e)

add_data_switches()

add_data_snooping()
