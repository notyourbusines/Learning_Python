# -*- coding: utf-8 -*-
'''
Задание 21.3b

Измените шаблон templates/ospf.txt из задания 21.3a таким образом,
чтобы для перечисленных переменных были указаны значения по умолчанию,
которые используются в том случае, если переменная не задана или,
если в переменной пустое значение.

Не использовать для этого выражения if/else.

Задать в шаблоне значения по умолчанию для таких переменных:
* process - значение по умолчанию 1
* ref_bw - значение по умолчанию 10000


Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf3.yml,
с помощью функции generate_cfg_from_template из задания 21.1-21.1c.
Не копируйте код функции.

'''
from jinja2 import Environment, FileSystemLoader, Template
import yaml
import sys
import json
import os
from task_21_1c import generate_cfg_from_template

generate_cfg_from_template('templates/ospf.txt', 'data_files/ospf3.yml')
