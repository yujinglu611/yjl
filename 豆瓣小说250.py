from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import bs4
import xlwt
import time
q=0

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('My Worksheet')
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'}
for i in range(0,251,25):
    time.sleep(1)
    url = ('https://book.douban.com/top250?start={}'.format(i))
    ret = Request(url, headers=header)
    html = urlopen(ret)
    bs = bs4.BeautifulSoup(html, 'html.parser')
    title=bs.find_all('table',{'width':'100%'})
    for titles in title:
    #name=titles.div.a.text.strip()
        name=titles.div.a['title']
        re_name=name.replace('\n','').replace(' ','')
        wr=titles.find('p',{'class':'pl'}).get_text().replace("\n","").replace(" ","").split("/")[0]
        cbs=titles.find('p',{'class':'pl'}).get_text().replace("\n","").replace(" ","").split("/")[-3]
        data=titles.find('p',{'class': 'pl'}).get_text().replace("\n", "").replace(" ", "").split("/")[-2]
        price=titles.find('p',{'class':'pl'}).get_text().replace("\n","").replace(" ","").split("/")[-1]
        pp = titles.find('span',{'class': 'pl'}).text.replace('(','').replace(')','').replace(' ','').replace('\n','')
        view=titles.find('span',{'class':'rating_nums'}).get_text()
        try:
            st=titles.find('span',{'class':'inq'}).text
        except:
            st=None
        worksheet.write(q, 0, label=re_name)
        worksheet.write(q, 1, label=wr)
        worksheet.write(q, 2, label=cbs)
        worksheet.write(q, 3, label=data)
        worksheet.write(q, 4, label=price)
        worksheet.write(q, 5, label=pp)
        worksheet.write(q, 6, label=view)
        worksheet.write(q, 7, label=st)
        workbook.save('豆瓣小说250.xls')
        q+=1
