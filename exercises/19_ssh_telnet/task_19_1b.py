# -*- coding: utf-8 -*-
'''
Задание 19.1b

Дополнить функцию send_show_command из задания 19.1a таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
'''
import yaml
import netmiko
from netmiko import ConnectHandler

command = 'sh ip int br'

def send_show_command(dev_to_send, commands_to_send):
    for each in dev_to_send:
        #print(each)
        try:
            with ConnectHandler(**each) as ssh:
                ssh.enable()
        
                result = ssh.send_command(commands_to_send)
                print(result)
                
        except netmiko.ssh_exception.NetMikoAuthenticationException:
            #incorrect credentials
            print('Authentication failed!')
            continue
        except netmiko.ssh_exception.NetMikoTimeoutException:
            #wrong IP address
            print('Connection Timeout for {} host!'.format(each['ip']))
            continue

with open('devices.yaml') as dev:
        devs_param = yaml.load(dev)
        for zzz in devs_param['routers']:
            #print(zzz)
            p = devs_param['routers']
        
send_show_command(p, command)
