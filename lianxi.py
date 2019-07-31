#coding=utf-8
import xlwt,xlrd
import time
from xlutils.copy import copy
import os,logging

class Excel():
    start =time.clock()
    c=['账号','密码','平均值']
    style=xlwt.easyxf('font: bold on')
    def filepath(self):
        c=time.strftime("%F")
        path=os.getcwd()+'\\file'  #获取文件地址
        if os.path.exists(path):
            pass
        else:
             os.mkdir(path)  #创建文件夹

        filpath =path+'\\'+c+'.xls'
        return filpath

    def book(self):
        try:
            self.wr=xlwt.Workbook()  #The name of the file created
        except Exception:
            print('文件创建失败，请检查创建的文件名是否存在！')
        for i in range(1,3):
            self.sh=self.wr.add_sheet("自动化"+str(i)) #添加sheet
        s=self.wr.get_sheet(0)
        s.write(0,0,self.c[0],self.style)  #写入的内容添加样式
        s.write(0,1,self.c[1],self.style)
        for i in range(1,1001):            #数据自增
            sj=int(8451252630000)+int(i)
            s.write(i,0,str(sj))           #写入内容
            s.write(i,1,'Faxuan.%1234')    #写入内容
        s1 = self.wr.get_sheet(1)     
        s1.write(0,0,self.c[2],self.style)
        self.wr.save(self.filepath())      #数据保存
    def avgsj(self):
        rb = xlrd.open_workbook(self.filepath())  #打开创建的Excel文件
        wb = copy(rb)                             #copy打开的Excel文件
        sheets=rb.sheets()[0]                     #
        c=sheets.col_values(0)                    #获取某一列的数据信息
        num=0
        for i in range(2,len(c)):                 #将获取的信息自动循环输出
            num=num+int(c[i])
        sheet0 = wb.get_sheet(0)
        sheet = wb.get_sheet(1)
        sheet0.write(0,0,self.c[0],self.style)
        sheet0.write(0,1,self.c[1],self.style)
        sheet.write(0,0,self.c[2],self.style)
        sheet.write(0,1,str(int(num/(len(c)-1))))  #在单元各种写入内容
        if os.path.exists(self.filepath()):        #判断当前文件夹下有没有这个文件，有就删除，然后进行保存
            os.remove(self.filepath())
            wb.save(self.filepath())
        else:
             wb.save(self.filepath())

    def booktime(self):                            
        self.logfile()
        path1 =os.getcwd()+'\\file\\'
        dirs = os.listdir(path1)                   #获取某个文件夹下的文件名称
        m = []
        for i in range(len(dirs)): 
            c = (os.path.join(path1, dirs[i]))
            m.append(c)
        for x in range(len(m)):                    #根据文件地址获取文件的创建时间
            dt = os.path.getctime(m[x])
            timeArray = time.localtime(dt)
            otherStyleTime = time.strftime("%Y-%m-%d", timeArray)     #文件时间截取展示
            if otherStyleTime == time.strftime("%F"):                 #判断获取的文件和系统的时间%F(是获取当前系统的时间：年月日)是否相等
                logging.info('No data found to delete')
                pass
            else:  
                os.remove(m[x])                                       #不一样就删除文件                                       
                logging.info('Successfully deleted files from the previous day '+ m[x])   

    def logfile(self):
        logging.basicConfig(level=logging.INFO,                       #日志格式定位,日志登记
                format='%(asctime)s %(levelname)s %(message)s',       #日志%(asctime)s：打印日志的时间，(levelname)s：打印日志级别，(message)s：打印日志信息
                datefmt='%a, %d %b %Y %H:%M:%S',                      #指定时间格式
                filename='info.log',                                  #输出日志的文件
                filemode='a')                                         #每次输出的日志累计显示，不更新

    def excelcom(self):
        self.booktime()
        self.book()
        self.avgsj()

w=Excel()
w.excelcom()