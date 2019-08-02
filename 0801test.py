#coding=utf-8

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import xlrd,os
from xlutils.copy import copy


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
path = os.getcwd() + '\\sj.xlsx'
rb = xlrd.open_workbook(path)
wb = copy(rb)
sheets = rb.sheets()[0]
c = sheets.col_values(0)
b = sheets.col_values(1)
d = sheets.col_values(2)

def cc():
    m=name_input.get()
    if m == 'admin':
        tk.Label(root, text='欢迎admin! 输入1查看会员 2添加会员 3删除会员 4 退出').place(x=90, y=80)
        tk.messagebox.showerror(message='欢迎admin! 输入1查看会员 2添加会员 3删除会员 4 退出')
        t1.place_forget()
        name_entry.place_forget()
    else:
        tk.messagebox.showerror(message='asdfas')

def lxone():
    t2 = tk.Label(root, text="请输入操作编号:")
    t2.place(x=80, y=120)
    name_input1 = tk.StringVar()
    name_entry1 = tk.Entry(root, bd=2, textvariable=name_input1)
    name_entry1.place(x=180, y=120)  # 设置文本栏
    m=name_input.get()
    if m=='1':
        ck()
    if m=='2':



def ck():

    root = Tk()  # 初始框的声明
    columns = ("ID", "账号", "添加时间")
    treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格
    treeview.column("ID", width=50, anchor='center')  # 表示列,不显示
    treeview.column("账号", width=100, anchor='center')
    treeview.column("添加时间", width=200, anchor='center')
    treeview.heading("ID", text="ID")  # 显示表头
    treeview.heading("账号", text="账号")
    treeview.heading("添加时间", text="添加时间")
    treeview.pack(side=LEFT, fill=BOTH)
    id = c[1:]
    zh = b[1:]
    ch = d[1:]
    for i in range(min(len(id), len(zh), len(ch))):  # 写入数据
        treeview.insert('', i, values=(id[i], zh[i], ch[i]))
    root.mainloop()

def addhy():





button1 = Button(root, text="确定",command=cc).pack(side=LEFT)
button2 = Button(root, text="退出", command=root.quit).pack(side=LEFT)
root.mainloop()