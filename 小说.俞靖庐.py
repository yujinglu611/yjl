from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import bs4
novel1=''
sum = 36212
for i in range(1,64):

    sum += 1
    url="https://www.uuzuowen.com/mingzhu/luanshijiaren/{}.html".format(str(sum))
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'}
    htmlAfter = Request(url, headers=header)
    html = urlopen(htmlAfter).read().decode('gbk')
    bs = BeautifulSoup(html, 'html.parser')
    novel=bs.find('div',{'class':'articleContent'})
    novel1=novel1+novel.get_text()
fo = open('1.text','wb')
fo.write((novel1).encode('utf-8'))
fo.close()
    #print(novel)