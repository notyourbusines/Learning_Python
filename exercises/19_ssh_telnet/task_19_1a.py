# -*- coding: utf-8 -*-
'''
Задание 19.1a

Переделать функцию send_show_command из задания 19.1 таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''

import yaml
import netmiko
from netmiko import ConnectHandler

command = 'sh ip int br'

def send_show_command(dev_to_send, commands_to_send):
    for each in dev_to_send:
        try:
            with ConnectHandler(**each) as ssh:
                ssh.enable()
        
                result = ssh.send_command(commands_to_send)
                print(result)
                
        except netmiko.ssh_exception.NetMikoAuthenticationException:
                #incorrect credentials
                print('Authentication failed!')
                continue

with open('devices.yaml') as dev:
        devs_param = yaml.load(dev)
        for zzz in devs_param['routers']:
            #print(zzz)
            p = devs_param['routers']
        
send_show_command(p, command)
