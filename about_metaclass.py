#! /usr/bin/env python3
# coding=utf-8

# 关于metaclass的一些代码

import sys
from logzero import logger

class People(type):
    def __new__(cls, class_name, class_bases, class_dic):
        logger.debug('People __new__')
        return type.__new__(cls, class_name, class_bases, class_dic)

    def __init__(self, class_name, class_bases, class_dic):
        logger.debug('People __init__')
        if class_name.islower():
            raise TypeError('类名必须使用驼峰体')
        doc = class_dic.get('__doc__')
        if doc is None or len(doc) == 0 or len(doc.strip('\n ')) == 0:
            raise TypeError('类体中必须有文档注释，且不能为空')

    def __call__(self, *args, **kwargs):
        logger.debug('People __call__')
        print("self: {!r}".format(self))

        p_obj = self.__new__(self)
        self.__init__(p_obj, *args, **kwargs)
        # p_obj=self(*args,**kwargs) # will recursion!

        return p_obj

class A:
    def a(self):return "echo from A#a"

class B:
    def b(self):return "echo from B#b"

class Employee(A,B,metaclass=People):
    '''
    111
    '''
    def __new__(cls):
        return object.__new__(cls)
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj=Employee('name',100)

assert obj.name=='name'
assert hasattr(obj,'a') and callable(getattr(obj,'a'))
assert hasattr(obj,'b') and callable(getattr(obj,'b'))

# 定义类的其他方式
def func(self):pass
Employeer=type('Employeer',(object,),dict(func=func))
assert Employeer.__name__=='Employeer'


class_body='''
"""
    doc
"""
def __init__(self,_id):
    print(_id)
'''
class_dic={}
exec(class_body,{},class_dic)
Employeer=People('Employeer',(A,B),class_dic) # 调用了 People的__init__, 先执行__new__
Employeer(41)

# 创建对象后初始化
class C:
    def __init__(self,_id):
        self._id=_id
obj=object.__new__(C)
C.__init__(obj,42)
print(obj._id)
