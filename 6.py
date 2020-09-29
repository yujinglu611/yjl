m=eval(input('请输入列表list:' ))
def even_num(x):
    list=[]
    for i in x:
            if i%2==0:
                list.append(i)
    return list
res=even_num(m)
print(res)