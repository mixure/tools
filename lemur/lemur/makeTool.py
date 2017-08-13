#! /usr/bin/env python
# coding=utf-8

"""获取设备信息,生成shell"""


import os
import commands
from string import Template
from string import maketrans


template=Template('''#! /usr/bin/env bash

monkey_shell='${monkey_shell}'

for serial_number in ${serial_numbers}
do
    echo "执行 $serial_number 设备"

    adb -s $serial_number shell $$monkey_shell>>$serial_number.$(date "+%Y.%m.%d.%H.%M").log
    
done

echo "日志记录在 $PWD"
''')

#获取设备serial_number
def serial_numbers():
    devices_info=commands.getoutput('adb devices')
    if 'not' in devices_info:
        return 'adb未安装或未找到'

    device_info= [device_info.split('\t')[0] 
                for device_info in devices_info.split('\n')[1:-1]
            ]
    return device_info if len(device_info) else '未插接手机/模拟器'


#根据模版生成shell
def render_and_dump(monkey_shell):
    echo=serial_numbers()
    if isinstance(echo,str):
        return echo


    table=maketrans(",",' ')
    shell=template.safe_substitute(monkey_shell=monkey_shell,
        serial_numbers=str(echo).translate(table,"[]'"))

    with open(os.path.sep.join([os.path.expanduser('~'),'lemur.sh']),
        'w') as f:
        f.write(shell)
    return '~/lemur.sh 已生成'
