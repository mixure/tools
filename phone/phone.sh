#! /usr/bash
# coding=utf-8

head='adb shell'

for body in ro.build.version.release\
            ro.build.version.sdk\
            ro.product.manufacturer\
            ro.product.name\
            ro.product.cpu.abilist\
            dalvik.vm.heapstartsize\
            dalvik.vm.heapgrowthlimit\
            dalvik.vm.heapsize;do
    echo  ${body##*.}: `$head getprop $body`
done

echo battery `$head dumpsys battery|grep level`

#package='com.android.browser'
if [ $package ];then

    echo cupinfo: `$head dumpsys cpuinfo|grep $package`
    echo `$head    dumpsys meminfo|grep $package`
    pid=`$head ps|grep $package|awk -F ' ' '{print $2}'`
    echo pid $pid
fi

# http://blog.csdn.net/subaohao/article/details/38730309
# adb shell am start -n xxx/xxx 

#  cpu  dumpsys cpuinfo  ; /proc/stat ;top
#  men  dumpsys meminfo 包名; 整体/proc/meminfo
#  battery dumpsys battery
#  /proc/${pid}/net/dev