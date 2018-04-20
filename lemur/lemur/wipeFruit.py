#! /usr/bin/env python
# coding=utf-8


"""数据判断,生成monkey shell"""


class WipeFruit:
    def check_fruit(self,cache):
        if not cache['count'][1]:
            return '执行次数必填'
        return 0

    def then_eat_it(self,cache):
        echo=self.check_fruit(cache)
        if echo:
            return echo

        shell=list(['adb','shell','monkey'])
        sum=0
        for name,(option,value,description) in cache.iteritems():
            if 'ig' in name:
                shell.append(option if value else '')
            elif option and value:
                    shell.extend([option,value])
            elif value:
                shell.append(value)

            try:
                if option and 'pct' in option and value:
                    sum+=int(value)
            except:
                return '你一定输入了个不能转成整数的东西,在%s那.' %description
        else:
            if sum>100:
                return '事件总数大于100%'
            return ' '.join(shell)
            pass
