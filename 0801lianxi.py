#coding=utf-8
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import xlrd,os
from xlutils.copy import copy

path = os.getcwd() + '\\sj.xlsx'
rb = xlrd.open_workbook(path)
wb = copy(rb)
sheets = rb.sheets()[0]
b = sheets.col_values(1)

root = tk.Tk()
root.title("添加")  #确定弹窗的title
root.geometry('450x300') #设置窗口大小
ft = ('黑体', 30, "bold")  #设置字体格式
tk.Label(root, text='添加', font=ft).place(x=150, y=30)  #设置标题内容
t1 = tk.Label(root, text="添加账号:")
t1.place(x=80, y=120)
name_input = tk.StringVar()
name_entry = tk.Entry(root, bd=2, textvariable=name_input)
name_entry.place(x=180, y=120)
for i in b[1:]:
    if(i == name_input):
        tk.messagebox.showerror(message='请重新输入')
    else:




