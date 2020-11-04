from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
texts=[]
titles=[]
url="http://www.cfbond.com/cfkx/index.html"
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'}
def updateurl(url,header):
    global bs
    bf=Request(url,headers=header)
    html=urlopen(bf)
    bs=bs4.BeautifulSoup(html,'html.parser')
ret=Request(url,headers=header)
html=urlopen(ret)
bs=BeautifulSoup(html,"html.parser")
title1=bs.find('ul',{'class':''})
for h in title1.find_all('li'):
    link=h.find('a')['href']
    titles.append(h.find('h2').get_text().replace('\n','').replace(' ','').replace('\r',''))
    updateurl(link,header)
    try:
        text=bs.find('div',{'class':'s_xlLContCRC'})
        texts.append(text.get_text())
    except:
        texts.append('None')
for i in range(len(titles)):
    print('{0:{2}<30}{1:{2}<100}'.format(titles[i],texts[i],chr(12288)))

    #print(link)

