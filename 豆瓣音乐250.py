from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
import xlwt
import time
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('My Worksheet')
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}
q=0
for i in range(0,226,25):
    time.sleep(1)
    url=("https://music.douban.com/top250?start={}".format(i))
    ret=Request(url,headers=header)
    html=urlopen(ret)
    bs=bs4.BeautifulSoup(html,'html.parser')
    title=bs.find_all('div',{'class':'pl2'})
    for titles in title:
        t=titles.find('a').get_text().replace("\n","").replace(" ","")
        n=titles.find('p',{'class':'pl'}).get_text().replace("\n","").replace(" ","").split("/")[0]
        x=titles.find('p', {'class': 'pl'}).get_text().replace("\n", "").replace(" ", "").split("/")[1]
        y=titles.find('p', {'class': 'pl'}).get_text().replace("\n", "").replace(" ", "").split("/")[-1]
        s=titles.find('span',{'class':'rating_nums'}).get_text()
        # print(t)
        # print(n)
        # print(x)
        # print(y)
        # print(s)
        worksheet.write(q, 0, label=t)
        worksheet.write(q, 1, label=n)
        worksheet.write(q, 2, label=x)
        worksheet.write(q, 3, label=y)
        worksheet.write(q, 4, label=s)
        workbook.save('豆瓣音乐250.xls')
        q+=1

