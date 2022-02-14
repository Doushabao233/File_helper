from tkinter import *
import os
import tkinter.messagebox as msg
import time

def merge(t, h):
    if t == '' or h == '':
        msg.showerror('错误', '没有填写完整')
    elif t == h:
        msg.showerror('错误', '目标图片与隐藏的文件相同')
        msg.showinfo('提示', '你想把自己塞进自己里头 这合理吗？')
    else:
        if '.' not in t:
            msg.showerror('错误', '没有填写后缀！')
        elif t.split('.')[1] == '':
            msg.showerror('错误', '你写错了')
        else:
            file_type = t.split('.')[1]
        os.system('copy {} {}'.format(t, 'export.{}'.format(file_type)))
        os.system('copy /b {}+{}'.format('export.{}'.format(file_type), h))
        msg.showinfo('成功', '文件制作完成！\n但我不能保证是否正确..请查看一下！')

def tips():
    msg.showinfo('用前必看', '请将文件放置于本程序同一个目录下，否则会找不到文件导致无法生成。')

w = Tk()
w.title('文件助手 - File Helper')
w.geometry('784x464')
w.resizable(False, False)

l = Label(text='文件小助手', font=('微软雅黑', 20))
l.place(x=340, y=40)

target_text = Label(text='目标文件:', font=('微软雅黑', 16), justify=LEFT)
target_text.place(x=215, y=126)
hide_text = Label(text='隐藏的文件:', font=('微软雅黑', 16), justify=LEFT)
hide_text.place(x=195, y=194)

target = Entry(width=18, font=('微软雅黑', 15))
target.place(x=320, y=130)
hide = Entry(width=18, font=('微软雅黑', 15))
hide.place(x=320, y=195)

tips_button = Button(text='用前必看', font=('仿宋', 20), command=tips)
tips_button.place(x=340, y=280)


ok_button = Button(text='开始制作', font=('仿宋', 20), command=lambda: merge(target.get(), hide.get()))
ok_button.place(x=340, y=360)
w.mainloop()