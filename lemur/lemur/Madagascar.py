#! /usr/bin/env python
# coding=utf-8


"""保存配置信息"""


import os.path
import pickle
from collections import OrderedDict


class Madagascar:
    def __init__(self):
        self.path=os.path.sep.join((os.path.expanduser('~'),'.lemur'))

    def dump(self,cache):
        
        with open(self.path,'w') as f:
            pickle.dump(cache,f)

    def load(self):
        if not os.path.exists(self.path):
            return OrderedDict([
            ('package_name',
                ['-p','','测试包名 -p com.xxx']),
            ('ig_crashes',
                ['--ignore-crashes',1,'忽略程序崩溃 --ignore-crashes']),
            ('touch',
                ['--pct-touch','','触摸事件 --pct-touch (%)']),
            ('motion',
                ['--pct-motion','','手势事件 --pct-motion (%)']),
            ('pinch',
                ['--pct-pinchzoom','','缩放事件:--pct-pinchzoom (%)']),
            ('trackball',
                ['--pct-trackball','','轨迹球事件:--pct-trackball (%)']),
            ('screen',
                ['--pct-rotation','','屏幕事件:--pct-rotation (%)']),
            ('nav',
                ['--pct-nav','','导航事件:--pct-nav (%)']),
            ('major',
                ['--pct-majornav','','主要事件:--pct-majornav (%)']),
            ('system',
                ['--pct-syskeys','','系统事件:--pct-syskeys (%)']),
            ('app',
                ['--pct-appswitch','','切屏事件:--pct-appswitch (%)']),
            ('keyboard',
                ['--pct-flip','','键盘事件:--pct-flip (%)']),
            ('anyevents',
                ['--pct-anyevent','','其他事件:--pct-anyevent (%)']),
            ('delay',
                ['--throttle','','延时 --throttle (ms)']),
            ('seed',
                ['-s','','随机种子 -s']),
            ('log_level',
                [None,'','日志级别 -v -v -v']),
            ('count',
                [None,'1000','执行次数 (必填)']),
            ])

        with open(self.path) as f:
            return pickle.load(f)

if __name__=='__main__':
    m=Madagascar()
    m.dump({'key':'value'})
    print m.load()
    pass
