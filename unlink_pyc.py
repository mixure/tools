# /usr/bin/env python
# coding=utf-8

import os,shutil
from logzero import logger

path=os.path.dirname(
    os.path.abspath(__file__))
exts=['.pyo','.pyc','.log','.html']


for dirname,subdirs,files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] in exts or 'log' in file:
            path=os.path.join(dirname,file)
            logger.debug(path)
            os.unlink(os.path.join(dirname,file))
