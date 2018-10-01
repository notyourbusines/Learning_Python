# -*- coding: utf-8 -*-
'''
Задание 19.2d

В этом задании надо создать функцию send_cfg_to_devices, которая выполняет команды на нескольких устройствах последовательно и при этом выполняет проверку на ошибки в командах.

Параметры функции:
* devices_list - список словарей с параметрами подключения к устройствам, которым надо передать команды
* config_commands - список команд, которые надо выполнить

Функция должна проверять результат на такие ошибки:
* Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка, функция должна выводить сообщение на стандартный поток вывода с информацией о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

После обнаружения ошибки, функция должна спросить пользователя надо ли выполнять эту команду на других устройствах.

Варианты ответа [y]/n:
* y - выполнять команду на оставшихся устройствах (значение по умолчанию)
* n - не выполнять команду на оставшихся устройствах

Функция send_cfg_to_devices должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - IP устройства
* значение - вложенный словарь:
  * ключ - команда
  * значение - вывод с выполнением команд

В файле задания заготовлены команды с ошибками и без:
'''
commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

error_msg = 'Incomplete command', 'Ambiguous command', 'Invalid input detected at'

failed_comms = {}
passed_comms = {}
rslt_fld = {}
rslt_pssd = {}
rslt_overall = []
import netmiko
import yaml
from netmiko import ConnectHandler

def send_config_command(dev_to_send, commands_to_send):
    for each in dev_to_send:
        IP_add = str(each['ip'])
        try:
            with ConnectHandler(**each) as ssh:
                ssh.enable()
                flag = False
                for pizda in commands_to_send:
                    if flag == True:
                        break
                    result = ssh.send_config_set(pizda)
                    for piska in error_msg:
                        if piska in result:
                            failed_comms[pizda] = result
                            rslt_fld['failed_comms_{}'.format(IP_add)] = failed_comms
                            print('Обнаружена ошибка {} при выполнении команды {}'.format(piska, pizda))
                            print('Выполнять эту команду для других устройств? [Y]/n')
                            inpt = input()
                            if inpt == 'Y':
                                break
                            else:
                                commands_to_send.remove(pizda)
                                #flag = True
                                break
                    else:
                        passed_comms[pizda] = result
                        rslt_pssd['passed_comms_{}'.format(IP_add)] = passed_comms
        except netmiko.ssh_exception.NetMikoAuthenticationException:
            #incorrect credentials
            print('Authentication failed!')
            continue
        except netmiko.ssh_exception.NetMikoTimeoutException:
            #wrong IP address
            print('Connection Timeout for {} host!'.format(each['ip']))
            continue
    rslt_overall = [rslt_pssd, rslt_fld]
    print(tuple(rslt_overall))

with open('devices.yaml') as dev:
        devs_param = yaml.load(dev)
        #print(devs_param['routers'])
        p = devs_param['routers']
        
zopa = send_config_command(p, commands)
