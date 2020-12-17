from urllib import request

from bs4 import BeautifulSoup
import json
from urllib.request import urlretrieve
import os
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

def fetch_data(url):
    req=request.Request(url)
    with request.urlopen(req) as f:
        return json.loads(f.read().decode('utf-8'))
ww=[]

t=0
j=0
for e in range(1,5):
    url='https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7415376365442300203&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%88%97%E7%BB%B4%E5%9D%A6%E9%A3%8E%E6%99%AF%E6%B2%B9%E7%94%BB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E5%88%97%E7%BB%B4%E5%9D%A6%E9%A3%8E%E6%99%AF%E6%B2%B9%E7%94%BB&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=1e&1608191355132='.format(e*30)
    data1=fetch_data(url)
    y=data1['data']
    # ww.append(y)
    # print(data1)

    for g in y:
        try:
            k=(g['thumbURL'])
            #print(k)
            ww.append(k)
        except:
            print('')

for i in ww:
    h=ww[j]
    j=j+1
    t=t+1
    url = '{}'.format(i)
    dir = os.path.abspath('.')
    work_path = os.path.join(dir, '{}.jpg').format(t)
    urlretrieve(url, work_path)
    # #print(i)
    # t=t+1
    # link=urlretrieve(k,path+'jsonpa\\image{}.jpg'.format(t))


