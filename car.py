#! /usr/bin/env python
# coding=utf-8

"""
压缩文件夹，上传到远程机器后解压；
远程机器文件夹压缩，取到本机解压；
"""
import sys,os
from fabric import Connection
import send2trash

remote_machince=''
passwd=''
dir_name='gaslight'
des_dir='/root/local/'

print('{}, okey?'.format(sys.argv[1]))
input()

c=Connection(remote_machince,connect_kwargs={'password':passwd})
if sys.argv[1]=='push':
    os.system('tar -czvf {0}.tar.gz {0}'.format(dir_name))
    with c.cd(des_dir):
        c.put('/Users/yeah/local/{}.tar.gz'.format(dir_name),
            des_dir)
        c.run('tar -xzvf {}.tar.gz'.format(dir_name))
        c.run('rm -f {}.tar.gz'.format(dir_name))
    os.system('rm -f {}.tar.gz'.format(dir_name))
if sys.argv[1]=='pull':
    with c.cd(des_dir):
        c.run('tar -czvf {0}.tar.gz {0}'.format(dir_name))
        c.get('{}{}.tar.gz'.format(des_dir,dir_name),
            '{}/local/{}.tar.gz'.format(os.path.expanduser('~'),
                dir_name))
    send2trash.send2trash(dir_name)
    os.system('tar -xzvf {}.tar.gz'.format(dir_name))
    os.system('rm -f {}.tar.gz'.format(dir_name))
