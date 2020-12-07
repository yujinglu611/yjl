

import math
import pandas as pd
import time
import requests




def get_json(url,num):
    '''''从网页获取JSON,使用POST请求,加上头部信息'''
    start_url = 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&sugin'
    my_headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Host':'www.lagou.com',
            'Referer':'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
            'X-Anit-Forge-Code':'0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With':'XMLHttpRequest'
            }

    my_data = {
            'first': 'true',
            'pn':num,
            'kd':'java'}
    cookies = requests.get(url=start_url, headers=my_headers).cookies
    res = requests.post(url, headers = my_headers, data = my_data,cookies=cookies)
    res.raise_for_status()
    res.encoding = 'utf-8'
    # 得到包含职位信息的字典
    page = res.json()
    return page


def get_page_num(count):
    '''''计算要抓取的页数'''
    # 每页15个职位,向上取整
    res = math.ceil(count/15)
    # 拉勾网最多显示30页结果
    if res > 30:
        return 30
    else:
        return res

def get_page_info(jobs_list):
    '''''对一个网页的职位信息进行解析,返回列表'''
    page_info_list = []
    for i in jobs_list:
        job_info = []
        job1=[]
        job2=[]
        job1.append(i['companyFullName'])
        job2.append(i['positionName'])
        #print(job1)

        job_info.append(i['companyFullName'])
        # job_info.append(i['companyShortName'])
        # job_info.append(i['companySize'])
        # job_info.append(i['financeStage'])
        # job_info.append(i['district'])
        job_info.append(i['positionName'])
        # job_info.append(i['workYear'])
        # job_info.append(i['education'])
        # job_info.append(i['salary'])
        # job_info.append(i['positionAdvantage'])
        page_info_list.append(job_info)

        import pymysql
        conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, database='mysql')
        cursor = conn.cursor()
        try:
            # 创建表格设置字段属性
            cursor.execute('CREATE TABLE TT (company VARCHAR(30) NOT NULL,job VARCHAR(30) NOT NULL)')
            print('成功建表')
        except:
            print('此表名已存在')
            conn.rollback()  # 失败则回滚数据
        for i in range(len(job1)):
            sql = '''insert into  TT (company,job) values ('%s','%s')''' % (job1[i], job2[i])

            print('插入' + str(i + 1) + '行')  # ''' ''' 一定要使用，不然会出现解析失败
            try:
                cursor.execute(sql)
                conn.commit()
            except:
                conn.rollback()
                print('写入失败')

        cursor.close()
        conn.close()
    return page_info_list

def main():
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
    # 先设定页数为1,获取总的职位数
    page_1 = get_json(url,1)
    total_count = page_1['content']['positionResult']['totalCount']
    num = get_page_num(total_count)
    total_info = []
    time.sleep(20)
    print('职位总数:{},页数:{}'.format(total_count,num))

    for n in range(1,num+1):
        # 对每个网页读取JSON, 获取每页数据
        page = get_json(url,n)
        jobs_list = page['content']['positionResult']['result']
        page_info = get_page_info(jobs_list)
        total_info += page_info
        #print(page_info)
        #print(total_info)
        #print(jobs_list)
        print('已经抓取第{}页, 职位总数:{}'.format(n, len(total_info)))
        # 每次抓取完成后,暂停一会,防止被服务器拉黑
        time.sleep(30)
    #将总数据转化为data frame再输出
    # df = pd.DataFrame(data = total_info,columns = ['公司全名','公司简称','公司规模','融资阶段','区域','职位名称','工作经验','学历要求','工资','职位福利'])
    df = pd.DataFrame(data=total_info, columns=['公司全名','职位名称'])
    df.to_csv('lagou_jobs.csv',index = False)
    print('已保存为csv文件.')

if __name__== "__main__":
    main()
