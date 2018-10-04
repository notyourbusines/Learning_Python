# -*- coding: utf-8 -*-
'''
Задание 19.4

Создать функцию send_commands_to_devices (для подключения по SSH используется netmiko).

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В этой функции должен использоваться список словарей, в котором не указаны имя пользователя, пароль, и пароль на enable (файл devices2.yaml).

Функция должна запрашивать имя пользователя, пароль и пароль на enable при старте.
Пароль не должен отображаться при наборе.

Функция send_commands_to_devices должна использовать функцию send_commands из задания 19.3.

'''

import netmiko
import yaml
from netmiko import ConnectHandler
import getpass
from task_19_3 import send_commands

with open('devices2.yaml') as dev:
    devs_param = yaml.load(dev)
    p = devs_param['routers']

def check_ping(device_to_check):
    reply = subprocess.run(['ping', '-c', '3', '-n', device_to_check])
    if reply.returncode == False:
        return True
    else:
        return False

def send_commands_to_devices(devices_list, show=False, filename=False, config=False):
    resulting_list = []
    uname = input('Please input username: ')
    print('Please input password: ')
    password = getpass.getpass()
    print('Please input enable password: ')
    enable_pwd = getpass.getpass()
    for each in devices_list:
        each['username'] = uname
        each['password'] = password
        each['secret'] = enable_pwd
        resulting_list.append(each)
    if show:
        print('Running SHOW command on devices: ')
        send_commands(resulting_list, show=True)
    elif filename:
        print('Running commands from file on devices: ')
        send_commands(resulting_list, filename=True)
    elif config:
        print('Running CONFIG command on devices: ')
        send_commands(resulting_list, config=True)

send_commands_to_devices(p, show=True)
