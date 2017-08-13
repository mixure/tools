# lemur

lemur是monkey shell的GUI程序.

存在问题:
1.对于任意的输入,几乎没怎么判断
2.不能保证在所有的平台下都能正常工作,它依赖于tk

安装:
1.python setup.py install 后,在命令行执行lemur
2.安装依赖于setuptools
3.若不能安装
   直接执行python lemur/lemur.py

执行环境:
py2

使用:
1.根据当前的输入生成adb monkey
2.可保存配置,记录在～.lemur
  保存配置后再次启动,会从 ～.lemur读取
3.根据当前插接的安卓设备和选项信息生成shell

ps:
 ui参考https://github.com/mixure/AndroidTools