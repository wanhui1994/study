#coding=utf-8
import xlwt,xlrd
import time
from xlutils.copy import copy
import os,logging

class Excel():
    start =time.clock()
    c=['�˺�','����','ƽ��ֵ']
    style=xlwt.easyxf('font: bold on')
    def filepath(self):
        c=time.strftime("%F")
        path=os.getcwd()+'\\file'  #��ȡ�ļ���ַ
        if os.path.exists(path):
            pass
        else:
             os.mkdir(path)  #�����ļ���

        filpath =path+'\\'+c+'.xls'
        return filpath

    def book(self):
        try:
            self.wr=xlwt.Workbook()  #The name of the file created
        except Exception:
            print('�ļ�����ʧ�ܣ����鴴�����ļ����Ƿ���ڣ�')
        for i in range(1,3):
            self.sh=self.wr.add_sheet("�Զ���"+str(i)) #���sheet
        s=self.wr.get_sheet(0)
        s.write(0,0,self.c[0],self.style)  #д������������ʽ
        s.write(0,1,self.c[1],self.style)
        for i in range(1,1001):            #��������
            sj=int(8451252630000)+int(i)
            s.write(i,0,str(sj))           #д������
            s.write(i,1,'Faxuan.%1234')    #д������
        s1 = self.wr.get_sheet(1)     
        s1.write(0,0,self.c[2],self.style)
        self.wr.save(self.filepath())      #���ݱ���
    def avgsj(self):
        rb = xlrd.open_workbook(self.filepath())  #�򿪴�����Excel�ļ�
        wb = copy(rb)                             #copy�򿪵�Excel�ļ�
        sheets=rb.sheets()[0]                     #
        c=sheets.col_values(0)                    #��ȡĳһ�е�������Ϣ
        num=0
        for i in range(2,len(c)):                 #����ȡ����Ϣ�Զ�ѭ�����
            num=num+int(c[i])
        sheet0 = wb.get_sheet(0)
        sheet = wb.get_sheet(1)
        sheet0.write(0,0,self.c[0],self.style)
        sheet0.write(0,1,self.c[1],self.style)
        sheet.write(0,0,self.c[2],self.style)
        sheet.write(0,1,str(int(num/(len(c)-1))))  #�ڵ�Ԫ����д������
        if os.path.exists(self.filepath()):        #�жϵ�ǰ�ļ�������û������ļ����о�ɾ����Ȼ����б���
            os.remove(self.filepath())
            wb.save(self.filepath())
        else:
             wb.save(self.filepath())

    def booktime(self):                            
        self.logfile()
        path1 =os.getcwd()+'\\file\\'
        dirs = os.listdir(path1)                   #��ȡĳ���ļ����µ��ļ�����
        m = []
        for i in range(len(dirs)): 
            c = (os.path.join(path1, dirs[i]))
            m.append(c)
        for x in range(len(m)):                    #�����ļ���ַ��ȡ�ļ��Ĵ���ʱ��
            dt = os.path.getctime(m[x])
            timeArray = time.localtime(dt)
            otherStyleTime = time.strftime("%Y-%m-%d", timeArray)     #�ļ�ʱ���ȡչʾ
            if otherStyleTime == time.strftime("%F"):                 #�жϻ�ȡ���ļ���ϵͳ��ʱ��%F(�ǻ�ȡ��ǰϵͳ��ʱ�䣺������)�Ƿ����
                logging.info('No data found to delete')
                pass
            else:  
                os.remove(m[x])                                       #��һ����ɾ���ļ�                                       
                logging.info('Successfully deleted files from the previous day '+ m[x])   

    def logfile(self):
        logging.basicConfig(level=logging.INFO,                       #��־��ʽ��λ,��־�Ǽ�
                format='%(asctime)s %(levelname)s %(message)s',       #��־%(asctime)s����ӡ��־��ʱ�䣬(levelname)s����ӡ��־����(message)s����ӡ��־��Ϣ
                datefmt='%a, %d %b %Y %H:%M:%S',                      #ָ��ʱ���ʽ
                filename='info.log',                                  #�����־���ļ�
                filemode='a')                                         #ÿ���������־�ۼ���ʾ��������

    def excelcom(self):
        self.booktime()
        self.book()
        self.avgsj()

w=Excel()
w.excelcom()