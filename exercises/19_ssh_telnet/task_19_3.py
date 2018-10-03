# -*- coding: utf-8 -*-
'''
Задание 19.3

Создать функцию send_commands (для подключения по SSH используется netmiko).

Параметры функции:
* device - словарь с параметрами подключения к устройству, которому надо передать команды
* show - одна команда show (строка)
* filename - имя файла, в котором находятся команды, которые надо выполнить (строка)
* config - список с командами, которые надо выполнить в конфигурационном режиме

В зависимости от того, какой аргумент был передан, функция вызывает разные функции внутри.
При вызове функции, всегда будет передаваться только один из аргументов show, config, filename.

Далее комбинация из аргумента и соответствующей функции:
* show - функция send_show_command из задания 19.1
* config - функция send_config_commands из задания 19.2
* filename - функция send_commands_from_file (ее надо написать по аналогии с предыдущими)

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - вывод с выполнением команд

Проверить работу функции на примере:
* устройств из файла devices.yaml (для этого надо считать информацию из файла)
* и различных комбинация аргумента с командами:
    * списка команд commands
    * команды command
    * файла config.txt

'''

import netmiko
import yaml
from netmiko import ConnectHandler

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
            
def send_show_command(dev_to_send, commands_to_send):
    rslt = {}
    for each in dev_to_send:
        #print(each)
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
    return rslt
            
def send_config_command(dev_to_send, commands_to_send):
    rslt = {}
    for each in dev_to_send:
        try:
            with ConnectHandler(**each) as ssh:
                ssh.enable()
                for pizda in commands_to_send:
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
            except netmiko.ssh_exception.NetMikoAuthenticationException:
                #incorrect credentials
                print('Authentication failed!')
                continue
            except netmiko.ssh_exception.NetMikoTimeoutException:
                #wrong IP address
                print('Connection Timeout for {} host!'.format(each['ip']))
                continue
    return rslt

send_commands(p, show=True)
