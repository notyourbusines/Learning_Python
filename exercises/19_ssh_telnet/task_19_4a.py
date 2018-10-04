# -*- coding: utf-8 -*-
'''
Задание 19.4a

Дополнить функцию send_commands_to_devices таким образом, чтобы перед подключением к устройствам по SSH,
выполнялась проверка доступности устройства pingом (можно вызвать команду ping в ОС).

> Как выполнять команды ОС, описано в разделе [subprocess](../../book/12_useful_modules/subprocess.md). Там же есть пример функции с отправкой ping.

Если устройство доступно, можно выполнять подключение.
Если не доступно, вывести сообщение о том, что устройство с определенным IP-адресом недоступно
и не выполнять подключение к этому устройству.

Для удобства можно сделать отдельную функцию для проверки доступности
и затем использовать ее в функции send_commands_to_devices.

'''
import netmiko
import yaml
from netmiko import ConnectHandler
import getpass
from task_19_3 import send_commands
import subprocess

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
    last_list = []
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
    for xyz in resulting_list:
        print('Текущий элемент списка: ', xyz)
        chpok = check_ping(xyz['ip'])
        if not chpok:
            continue
        else:
            last_list.append(xyz)
    #print(last_list)
    if show:
        #print('Running SHOW command on devices: ')
        send_commands(last_list, show=True)
    elif filename:
        print('Running commands from file on devices: ')
        send_commands(last_list, filename=True)
    elif config:
        print('Running CONFIG command on devices: ')
        send_commands(last_list, config=True)

send_commands_to_devices(p, show=True)
