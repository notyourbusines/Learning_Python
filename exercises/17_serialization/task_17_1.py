# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает аргумент output в котором находится вывод команды sh version (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

Функция write_to_csv:
* ожидает два аргумента:
 * имя файла, в который будет записана информация в формате CSV
 * данные в виде списка списков, где:
    * первый список - заголовки столбцов,
    * остальные списки - содержимое
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает

Остальное содержимое скрипта может быть в скрипте, а может быть в ещё одной функции.

Скрипт должен:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в файл routers_inventory.csv

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

import glob
import re
import csv

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

def parse_sh_version():
    lst_list = []
    for each in sh_version_files:
        tmp_rslt = []
        host_name = re.search('r\d', each)
        #print(host_name)
        if host_name.group() == 'r1':
            tmp_rslt.append('r1')
        elif host_name.group() == 'r2':
            tmp_rslt.append('r2')
        elif host_name.group() == 'r3':
            tmp_rslt.append('r3')
        with open(each) as f:
            for line_s in f:
                ios_regex = re.search('Version (?P<ios>\d+.\d\(\d+\)\w+)', line_s)
                image = re.search('file is \"(?P<image>\S+)\"', line_s)
                uptime = re.search('uptime is (?P<uptime>\d+ days, \d+ hours, \d+ minutes)', line_s)
                if ios_regex:
                    tmp_rslt.append(ios_regex.group('ios'))
                elif image:
                    tmp_rslt.append(image.group('image'))
                elif uptime:
                    uptm = uptime.group('uptime')
                    uptm = uptm.replace(',', '')
                    tmp_rslt.append(uptm)
        lst_list.append(tmp_rslt)
    #print(lst_list)
    return(lst_list)

def write_to_csv(filenm, datanm):
    with open(filenm, 'w') as z:
        writer = csv.writer(z)
        for line_z in zaloopa:
            writer.writerow(line_z)

zaloopa = parse_sh_version()
zaloopa.append(headers)
zaloopa.reverse()
write_to_csv('routers_inventory.csv', zaloopa)
print(zaloopa)


