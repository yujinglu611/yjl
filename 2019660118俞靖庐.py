from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
texts=[]
titles=[]
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
for i in range(2,6):
    url = "http://www.cfbond.com/in/cfkxlb/index_{}.shtml".format(i)
    ret=Request(headers=header,url=url)
    html=urlopen(ret)
    bs=bs4.BeautifulSoup(html,'html.parser')
    alls=bs.find_all('li')
    for x in alls:
        titles.append(x.find('h2',class_='pubList_tit').get_text().replace('\r','').replace(' ','').replace('\n',''))
        url=x.find('a')['href']
        ret=Request(headers=header,url=url)
        html=urlopen(ret)
        bs=bs4.BeautifulSoup(html,'html.parser')
        try:
            texts.append(bs.find('div',class_='s_xlLContCRC').get_text().replace('\r','').replace(' ','').replace('\n','').replace('\t',''))
        except:
            texts.append('None')
with open('财富网.txt','a',encoding='utf-8') as c:
    for num in range(1,len(titles)+1):
        c.write('{0} {1}\n{2}\n'.format(num,titles[num-1],texts[num-1]))