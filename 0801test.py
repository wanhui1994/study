#coding=utf-8

from tkinter import *
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("操作wh")  #确定弹窗的title
root.geometry('450x300') #设置窗口大小
ft = ('黑体', 30, "bold")  #设置字体格式
tk.Label(root, text='小程序', font=ft).place(x=150, y=30)  #设置标题内容
t1 = tk.Label(root, text="请输入访问账号:")
t1.place(x=80, y=120)
name_input = tk.StringVar()
name_entry = tk.Entry(root, bd=2, textvariable=name_input)
name_entry.place(x=180, y=120)  #设置文本栏

def cc():
    m=name_input.get()
    if m == 'admin':
        tk.Label(root, text='欢迎admin! 输入1查看会员 2添加会员 3删除会员 4 退出').place(x=90, y=80)
        tk.messagebox.showerror(message='欢迎admin! 输入1查看会员 2添加会员 3删除会员 4 退出')
        t1.place_forget()
        name_entry.place_forget()



    else:
        tk.messagebox.showerror(message='asdfas')
def lxone(self):
    t2 = tk.Label(root, text="请输入操作编号:")
    t2.place(x=80, y=120)
    name_input1 = tk.StringVar()
    name_entry1 = tk.Entry(root, bd=2, textvariable=name_input1)
    name_entry1.place(x=180, y=120)  # 设置文本栏
    m=name_input.get()
    if m==1:
        print()




button1 = Button(root, text="确定",command=cc).pack(side=LEFT)
button2 = Button(root, text="退出", command=root.quit).pack(side=LEFT)
root.mainloop()