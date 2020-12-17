from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
url="http://cjc.ict.ac.cn/qwjs/No2020-01.htm"
ret=Request(url,headers=headers)
html=urlopen(ret)
bs=BeautifulSoup(html,'html.parser')
pic=bs.find('div',{'class':"Section1"})
title = pic.find_all('span', {'style': 'color:#006688'})
t=[]
j=0
for y in title:
        t.append(y.get_text().encode('iso-8859-1').decode('gbk'))
for i in pic.find_all('a'):
        i=i.attrs['href']
        url = '{}'.format(i)
        dir = os.path.abspath('.')
        k=t[j]
        j=j+1
        work_path = os.path.join(dir, '{}.pdf').format(k)
        urlretrieve(url, work_path)


