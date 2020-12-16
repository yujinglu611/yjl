from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
url="https://www.sohu.com/a/286956359_301394"
ret=Request(url,headers=headers)
html=urlopen(ret)
bs=BeautifulSoup(html,'html.parser')
pic=bs.find('article',{'class':"article"})
c=[]
t=0
for i in pic.find_all('img'):
    i=i.attrs['src']
    t=t+1
    url = '{}'.format(i)
    dir = os.path.abspath('.')
    work_path = os.path.join(dir, '{}.jpeg').format(t)
    urlretrieve(url, work_path)


