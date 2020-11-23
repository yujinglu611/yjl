import tkinter as tk
import random
import threading
import time
import xlrd
workbook = xlrd.open_workbook("11.xlsx")  # 读取表格
Data_sheet = workbook.sheets()[0]  # 读取sheet1
xuehao_list=Data_sheet.col_values(0)
name_list = Data_sheet.col_values(1)  # 读取第二列
import pymysql
conn=pymysql.connect(host='localhost',user='root',password='123456',port=3306,database='mysql')
cursor=conn.cursor()
try:
    #创建表格设置字段属性
    cursor.execute('CREATE TABLE sss (Stu_id VARCHAR(20) NOT NULL,Stu_name VARCHAR(20) NOT NULL)')
    print('成功建表')
except:
    print('此表名已存在')
    conn.rollback() # 失败则回滚数据
for i in range(len(xuehao_list)):
    sql = '''insert into  sss (Stu_id,Stu_name) values ('%s','%s')''' %(xuehao_list[i],name_list[i])

    print('插入' + str(i + 1) + '行')  # ''' ''' 一定要使用，不然会出现解析失败
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        print('写入失败')

cursor.close()
conn.close()
import pygame
import sqlite3
from win32com.client import Dispatch
speaker = Dispatch("SAPI.SpVoice")
# # 音乐的路径
# file = r'C:\Users\apple\Desktop\aa.mp3.mp3'
# # 初始化
# pygame.mixer.init()
# # 加载音乐文件
# track = pygame.mixer.music.load(file)
# # 开始播放音乐流
# pygame.mixer.music.play()

window = tk.Tk()
window.title('随机提问')
window.geometry('500x300')
window.resizable(False,False)
window.flag = True
first = tk.Label(window, text='', font=("宋体", 20, "normal"))
first.place(x=180,y=80,width=80,height=60)

second = tk.Label(window,text='',font = ("宋体", 20,"normal"))
second['fg'] = 'red'
second.place(x=180,y=150,width=80,height=60)

third = tk.Label(window,text='',font = ("宋体", 20,"normal"))
third.place(x=180,y=220,width=80,height=60)


#students=  ['周嘉铖','钱珑超','徐展','尤桉哲','钱涛','黄舒怡','胡志辉','吴昭耀','陈萌萌','郑巧悦','陈艳','梁明皓','蒋俊超','徐颖','倪宏涛','潘梦倩','俞靖庐','王中阳','毛贞强','张嫒','朱速航','陈涛','陆元超','叶振雄','奚申杰','叶梦婷','徐丽丽','潘艳']

def switch():
    window.flag=True
    fir=True
    lst=[]
    while window.flag and fir:
        i=random.randint(0, len(students)-1)
        first['text']=second['text']
        second['text']=third['text']
        third['text']=students[i]
        lst.append(first['text'])
        lst.append(second['text'])
        lst.append(third['text'])
        time.sleep(0.05)
        fir=False
    while window.flag and not fir:
        while students[i] in lst:
            i=random.randint(0, len(students)-1)
        lst=[]
        first['text']=second['text']
        second['text']=third['text']
        third['text']=students[i]
        lst.append(first['text'])
        lst.append(second['text'])
        lst.append(third['text'])
        time.sleep(0.05)
def butStartClick():
    t=threading.Thread(target=switch)
    t.start()


b = tk.Button(window, text='开始', command=butStartClick,font=('Arial,12'),width=10, height=1)
b.place(x=100,y=30)

def btnStopClick():
    window.flag=False
    speaker.Speak(second['text'])
s = tk.Button(window,text='停止', command=btnStopClick, font= ('Arial,12'), width=10, height=1)
s.place(x=260,y=30)
window.mainloop()