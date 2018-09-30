# -*- coding: utf-8 -*-
'''
Задание 19.2b

В этом задании необходимо переделать функцию send_config_commands из задания 19.2a или 19.2 и добавить проверку на ошибки.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * Invalid input detected, Incomplete command, Ambiguous command

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

При этом, параметр verbose также должен работать, но теперь он отвечает за вывод
только тех команд, которые выполнились корректно.

Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Отправить список команд commands на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_config_commands.

Примеры команд с ошибками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#i
% Ambiguous command:  "i"

В файле задания заготовлены команды с ошибками и без:
'''

commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands
#print(commands)
error_msg = 'Incomplete command', 'Ambiguous command', 'Invalid input detected at'

failed_comms = {}
passed_comms = {}
rslt_fld = {}
rslt_pssd = {}
rslt_overall = []
import netmiko
import yaml
from netmiko import ConnectHandler

import netmiko
import yaml
from netmiko import ConnectHandler

def send_config_command(dev_to_send, commands_to_send):
    for each in dev_to_send:
        IP_add = str(each['ip'])
        try:
            with ConnectHandler(**each) as ssh:
                ssh.enable()
                for pizda in commands_to_send:
                    result = ssh.send_config_set(pizda)
                    for piska in error_msg:
                        #print(piska)
                        if piska in result:
                            failed_comms[pizda] = result
                            rslt_fld['failed_comms_{}'.format(IP_add)] = failed_comms
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

print(zopa)
        
