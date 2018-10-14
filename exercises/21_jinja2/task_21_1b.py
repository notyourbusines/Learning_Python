# -*- coding: utf-8 -*-
'''
Задание 21.1b

Дополнить функцию generate_cfg_from_template из задания 21.1 или 21.1a:
* добавить поддержку разных форматов для файла с данными

Должны поддерживаться такие форматы:
* YAML
* JSON
* словарь Python

Сделать для каждого формата свой параметр функции.
Например:
* YAML - yaml_file
* JSON - json_file
* словарь Python - py_dict

Проверить работу функции на шаблоне templates/for.txt и данных:
* data_files/for.yml
* data_files/for.json
* словаре data_dict

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

def generate_cfg_from_template(template_dir, varibls, format=yaml, **args):
    
    tmp_dir, tmplate = os.path.split(template_dir)
    #print(args)
    
    env = Environment(loader=FileSystemLoader(tmp_dir), trim_blocks=True)
    template = env.get_template(tmplate)
    
    if format == 'yaml':
        #print('Попал на YAML')
        variables = yaml.load(open(varibls))
        print(template.render(variables))
    elif format == 'json':
        variables = json.load(open(varibls))
        print(template.render(variables))
    elif format == 'py_dict':
        variables = data_dict
        print(template.render(variables))
            
    
generate_cfg_from_template('templates/for.txt', 'data_files/for.json', format='py_dict')
