#coding=utf-8

from tkinter import *
import tkinter as tk


root = tk.Tk()
root.title("操作wh")
root.geometry('450x300')
ft=('黑体',30,"bold")
tk.Label(root,text='小程序',font=ft).grid(row=0)
tk.Label(root,text="请输入访问账号:").grid(row=1)
v1 = tk.StringVar()
tk.Entry(root,bd=2,textvariable=v1).grid(row=1,column=1)

# user_text = tk.Entry(root,bd=2,textvariable=v1).place(x=180,y=100)
#
#
# button1 = Button(root, text="确定",command=getuser).pack(side=LEFT)
# button2 = Button(root, text="退出", command=root.quit).pack(side=LEFT)
root.mainloop()






