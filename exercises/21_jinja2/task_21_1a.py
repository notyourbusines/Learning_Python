# -*- coding: utf-8 -*-
'''
Задание 21.1a

Дополнить функцию generate_cfg_from_template из задания 21.1:

Функция generate_cfg_from_template должна принимать любые аргументы,
которые принимает класс Environment и просто передавать их ему.

То есть, надо добавить возможность контролировать аргументы trim_blocks, lstrip_blocks
и любые другие аргументы Environment через функцию generate_cfg_from_template.

Проверить функциональность на аргументах:
* trim_blocks
* lstrip_blocks

'''

from jinja2 import Environment, FileSystemLoader, Template
import yaml
import sys
import os

def generate_cfg_from_template(template_dir, varibls, **args):
    
    tmp_dir, tmplate = os.path.split(template_dir)
    print(args)
    zzz = ''
    env = Environment(loader=FileSystemLoader(tmp_dir), trim_blocks=True)
    template = env.get_template(tmplate)
    
    variables = yaml.load(open(varibls))
    
    print(template.render(variables))
    
generate_cfg_from_template('templates/for.txt', 'data_files/for.yml', lstrip_blocks=True)
