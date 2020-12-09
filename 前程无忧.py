from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
import json
import re
import xlwt
workbook=xlwt.Workbook(encoding='utf-8')
worksheet=workbook.add_sheet('My Worksheet')
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
for k in range(1,6):
    o=k-1
    url = ("https://search.51job.com/list/080200,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,{}.html".format(k))
    ret=Request(headers=header,url=url)
    html=urlopen(ret)
    bs=bs4.BeautifulSoup(html,'html.parser')
#findcompany=re.compile(r'"company_name":"(.*?)",')
#findjob=re.compile(r'"job_name":"(.*?)",')
    names=bs.find_all('script',{'type':'text/javascript'})

    for name in names:
        t = name.get_text().replace('window.__SEARCH_RESULT__ = ', '')
        if len(t)>0:
            t2=json.loads(t)
        #print(t2)
            y=t2['engine_search_result']
            for i in range(0,len(y)):
                a=y[i]['company_name']
                b=y[i]['providesalary_text']
                c=y[i]['workarea_text']
                d=y[i]['jobwelf']
                e=y[i]['jobwelf_list']
                f=y[i]['job_href']
                url1=f
                info=Request(headers=header,url=url1)
                html=urlopen(info)
                bs = bs4.BeautifulSoup(html, 'html.parser')
                zhize=bs.find_all('div',{'class':'bmsg job_msg inbox'})
                for g in zhize:
                    h=g.get_text()
                    worksheet.write(i+o*len(y),5,label=h)
                worksheet.write(i+o*len(y), 0, label=a)
                worksheet.write(i+o*len(y), 1, label=b)
                worksheet.write(i+o*len(y), 2, label=c)
                worksheet.write(i+o*len(y), 3, label=d)
                worksheet.write(i+o*len(y), 4, label=e)
workbook.save('Excel_test.xls')