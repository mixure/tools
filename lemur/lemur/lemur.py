#! /usr/bin/env python
# coding=utf-8


import Tkinter as tk
from collections import OrderedDict

from Madagascar import Madagascar
from wipeFruit import WipeFruit
from makeTool import render_and_dump


class Lemur:
    def __init__(self,master):
        self.wf=WipeFruit()
        self.Mad=Madagascar()

        self.master=master
        self.master.title('lemur')

        self.cache=self.Mad.load()
        self.run()

    def run(self):
        index=1
        for name,(option,value,description) in self.cache.iteritems():
            if 'ig'  in name:
                setattr(self,name+'V',tk.IntVar())
                setattr(self,name,
                        tk.Checkbutton(self.master,
                                       text=description,
                                       variable=getattr(self,name+'V')
                                      )
                       )
                getattr(self,name).grid(row=index,column=0)
                if value==1:
                    getattr(self,name).select()
                else:
                    getattr(self,name).deselect()
            else:
                tk.Label(self.master,text=description).grid(row=index)
                setattr(self,name,tk.Entry(self.master))
                getattr(self,name).grid(row=index, column=1)
                getattr(self,name).insert(0,value)
            index+=1

        index+=1
        #输出结果文本框
        self.text=tk.Text(self.master, width=50,heigh=3,fg='BLUE')
        self.text.grid(row=index,column=0,columnspan=4)

        #生成monkey shell按钮
        index+=1
        adb_shell=tk.Button(self.master,
                            text='生成 adb monkey',
                            command=
                            lambda :self.show_msg(self.grab_adb_shell()))
        adb_shell.grid(row=index,column=0)

        #保存配置信息按钮
        save_config=tk.Button(self.master,
                              text='保存配置',
                              command=self.save_config)
        save_config.grid(row=index,column=1)

        #生成脚本按钮
        index+=1
        generate_shell=tk.Button(self.master,
                              text='生成 shell 脚本',
                              command=self.generate_shell)
        generate_shell.grid(row=index,column=0)

    def update_cache(self):
        for name in self.cache:
            self.cache[name][1]=getattr(self,
                    name+'V' if 'ig' in name else name).get()

    #生成monkey shell
    def grab_adb_shell(self):
        self.update_cache()
        return self.wf.then_eat_it(self.cache)

    #保存配置事件
    def save_config(self):
        self.update_cache()
        echo=self.grab_adb_shell()
        if 'adb' in echo:
            self.Mad.dump(self.cache)
            self.show_msg('配置已保存')
        else:
            self.show_msg(echo)

    #生成脚本事件
    def generate_shell(self):
        echo=self.grab_adb_shell()
        if 'adb' in echo:
            self.show_msg(render_and_dump(echo[10:]))
        else:
            self.show_msg(echo)

    #文本框显示事件
    def show_msg(self,content):
        self.text.delete('1.0',tk.END)
        self.text.insert('1.0',content)


def main():
    root=tk.Tk()
    monkey=Lemur(root)
    root.mainloop()


if __name__=='__main__':
    main()
