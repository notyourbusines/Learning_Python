# -*- coding: utf-8 -*-
'''
Задание 21.1c

Переделать функцию generate_cfg_from_template из задания 21.1, 21.1a или 21.1b:
* сделать автоматическое распознавание разных форматов для файла с данными
* для передачи разных типов данных, должен использоваться один и тот же параметр data

Должны поддерживаться такие форматы:
* YAML - файлы с расширением yml или yaml
* JSON - файлы с расширением json
* словарь Python

Если не получилось определить тип данных, вывести сообщение error_message (перенести текст сообщения в тело функции), завершить работу функции и вернуть None.

Проверить работу функции на шаблоне templates/for.txt и данных:
* data_files/for.yml
* data_files/for.json
* словаре data_dict

'''

error_message = '''
Не получилось определить формат данных.
Поддерживаются файлы с расширением .json, .yml, .yaml и словари Python
'''

data_dict = {
    'vlans': {
        10: 'Marketing',
        20: 'Voice',
        30: 'Management'
    },
    'ospf': [{
        'network': '10.0.1.0 0.0.0.255',
        'area': 0
    }, {
        'network': '10.0.2.0 0.0.0.255',
        'area': 2
    }, {
        'network': '10.1.1.0 0.0.0.255',
        'area': 0
    }],
    'id': 3,
    'name': 'R3'
}


from jinja2 import Environment, FileSystemLoader, Template
import yaml
import sys
import json
import os

def generate_cfg_from_template(template_dir, varibls, **args):
    
    tmp_dir, tmplate = os.path.split(template_dir)
    #print(args)
    
    env = Environment(loader=FileSystemLoader(tmp_dir), trim_blocks=True)
    template = env.get_template(tmplate)
    
    if 'yml' in varibls:
        #print('Попал на YAML')
        variables = yaml.load(open(varibls))
        print(template.render(variables))
    elif 'json' in varibls:
        variables = json.load(open(varibls))
        print(template.render(variables))
    elif 'py_dict' in varibls:
        variables = data_dict
        print(template.render(variables))
    else:
        print(error_message)
            
    
generate_cfg_from_template('templates/for.txt', 'py_dict')
