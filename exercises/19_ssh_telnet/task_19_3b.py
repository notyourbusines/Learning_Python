# -*- coding: utf-8 -*-
'''
Задание 19.3b


Дополнить функцию send_commands таким образом, чтобы перед подключением к устройствам по SSH,
выполнялась проверка доступности устройства pingом (можно вызвать команду ping в ОС).

> Как выполнять команды ОС, описано в разделе 11_modules/subprocess.html. Там же есть пример функции с отправкой ping.

Если устройство доступно, можно выполнять подключение.
Если не доступно, вывести сообщение о том, что устройство с определенным IP-адресом недоступно
и не выполнять подключение  к этому устройству.

Для удобства можно сделать отдельную функцию для проверки доступности
и затем использовать ее в функции send_commands.
'''

import netmiko
import yaml
from netmiko import ConnectHandler
import subprocess

commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]
command = 'sh ip int br'

def send_commands(device, show=False, filename=False, config=False):
    if show:
        zaloopec = send_show_command(p, command)
        print(zaloopec)
    elif filename:
        zaloopec = send_from_filename(p, 'config.txt')
        print(zaloopec)
    elif config:
        zaloopec = send_config_command(p, commands)
        print(zaloopec)
    


with open('devices.yaml') as dev:
    devs_param = yaml.load(dev)
    for zzz in devs_param['routers']:
        #print(zzz)
        p = devs_param['routers']
        
def check_ping(device_to_check):
    reply = subprocess.run(['ping', '-c', '3', '-n', device_to_check])
    if reply.returncode == False:
        return True
    else:
        return False
            
def send_show_command(dev_to_send, commands_to_send):
    rslt = {}
    for each in dev_to_send:
        #print(each)
        zopka = check_ping(each['ip'])
        #print(zopka)
        if zopka:
            try:
                with ConnectHandler(**each) as ssh:
                    ssh.enable()
                    result = ssh.send_command(commands_to_send)
                    tmp_ip = each['ip']
                    rslt[tmp_ip] = result
            except netmiko.ssh_exception.NetMikoAuthenticationException:
                #incorrect credentials
                print('Authentication failed!')
                continue
            except netmiko.ssh_exception.NetMikoTimeoutException:
                #wrong IP address
                print('Connection Timeout for {} host!'.format(each['ip']))
                continue
        else:
            continue
    return rslt
            
def send_config_command(dev_to_send, commands_to_send):
    rslt = {}
    for each in dev_to_send:
        zopka = check_ping(each['ip'])
        #print(each)
        if zopka:
            try:
                with ConnectHandler(**each) as ssh:
                    for pizda in commands_to_send:
                        ssh.enable()
                        result = ssh.send_config_set(pizda)
                        tmp_ip = each['ip']
                        rslt[tmp_ip] = result
            except netmiko.ssh_exception.NetMikoAuthenticationException:
                #incorrect credentials
                print('Authentication failed!')
                continue
            except netmiko.ssh_exception.NetMikoTimeoutException:
                #wrong IP address
                print('Connection Timeout for {} host!'.format(each['ip']))
                continue
        else:
            continue
        return rslt

def send_from_filename(dev_to_send, filenm):
    rslt = {}
    for each in dev_to_send:
        with open(filenm) as f:
            try:
                with ConnectHandler(**each) as ssh:
                    ssh.enable()
                    #print(each)
                    for pepiska in f:
                        result = ssh.send_config_set(pepiska)
                        tmp_ip = each['ip']
                        rslt[tmp_ip] = result
                        print(rslt)
            except netmiko.ssh_exception.NetMikoAuthenticationException:
                #incorrect credentials
                print('Authentication failed!')
                continue
            except netmiko.ssh_exception.NetMikoTimeoutException:
                #wrong IP address
                print('Connection Timeout for {} host!'.format(each['ip']))
                continue
    return rslt

send_commands(p, filename=True)
