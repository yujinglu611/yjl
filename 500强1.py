from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
count=0
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
url="http://www.fortunechina.com/fortune500/c/2020-08/10/content_372148.htm"
ret=Request(url,headers=headers)
html=urlopen(ret)
bs=BeautifulSoup(html,'html.parser')
info=bs.find('tbody')
infolist=[]
for over in info.find_all('td'):
    infonew=over.get_text().replace('\n','').replace('+','')
    infolist.append(infonew)
while '' in infolist:
    infolist.remove('')
for i in range(0,len(infolist),5):
    print('{0:^10} {1:^10} {2:^10} {3:{5}<10} {4:{5}^10}'.format(infolist[i],infolist[i+2],infolist[i+3],infolist[i+4],infolist[i+1],chr(12288)))