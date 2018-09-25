# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - результат выполнения команды

Отправить команду command на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_show_command.

'''
import yaml
from netmiko import ConnectHandler

command = 'sh ip int br'

def send_show_command(dev_to_send, commands_to_send):
    for each in dev_to_send:
        with ConnectHandler(**each) as ssh:
            ssh.enable()
            
            result = ssh.send_command(commands_to_send)
            print(result)

with open('devices.yaml') as dev:
        devs_param = yaml.load(dev)
        for zzz in devs_param['routers']:
            print(zzz)
            p = devs_param['routers']
        
send_show_command(p, command)
