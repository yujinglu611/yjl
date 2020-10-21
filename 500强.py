from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
url="http://www.fortunechina.com/fortune500/c/2020-08/10/content_372148.htm"
ret=Request(url,headers=headers)
html=urlopen(ret)
bs=BeautifulSoup(html,'html.parser')
wb=bs.find('tbody')#提取标签里的信息
""""将爬取的内容合并再换行"""
list1=[]
list2=[]
list3=[]
list4=[]
ran=0
for i in wb:
    ran+=1
    if ran%2==0:
        cot=0
        for a in i:
            cot+=1
            if cot==4:
                list1.append(a.get_text())
            elif cot==6:
                list2.append(a.get_text())
            elif cot==8:
                list3.append(a.get_text())
            elif cot==10:
                list4.append(a.get_text())
for i in range(0,500):
    print('{0:^10} {1:^10} {2:^10} {3:{5}<10} {4:{5}^10}'.format(i+1,list2[i],list3[i],list4[i],list1[i],chr(12288)))


