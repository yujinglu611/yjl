# coding:utf-8
yjl = {'2019660101': '周嘉铖','2019660103': '钱珑超','2019660104':'徐展','2019660105': '尤桉哲','2019660106': '钱涛','2019660107': '黄舒怡','2019660108': '胡志辉','2019660109': '吴昭耀','2019660110': '陈萌萌','2019660111': '郑巧悦','2019660112': '陈艳','2019660113': '梁明皓','2019660114': '蒋俊超','2019660115': '徐颖','2019660116': '倪宏涛','2019660117': '潘梦倩','2019660118': '俞靖庐','2019660119': '王中阳','2019660120': '毛贞强','2019660121': '张嫒','2019660123': '朱速航','2019660124': '陈涛',"2019660125": '陆元超','2019660126': '叶振雄','2019660127': '奚申杰','2019660128': '叶梦婷','2019660129': '徐丽丽','2019660130':'潘艳'}
#print(len(dict))
#list = [2019660101,2019660103,2019660104,2019660105,2019660106,2019660107,2019660108,2019660109,2019660110,2019660111,2019660112,2019660113,2019660114,2019660115,2019660116,2019660117,2019660118,2019660119,2019660120,2019660121,2019660123,2019660124,2019660125,2019660126,2019660127,2019660128,2019660129,2019660130]
import random
n= int(input('请输入要抽取的人数：'))
a = random.sample(yjl.keys(), n)
for i in a:
    print(i,yjl[i])