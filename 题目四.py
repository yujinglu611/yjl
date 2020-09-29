list1 = [1,2,6,0.3,2,0.5,8-1,2.4]
for i in range(len(list1)-1):        #循环遍历从0开始到倒数第二个元素下标
    for j in range(len(list1)-1-i):       #循环遍历从0开始，每次循环将最大数放到最末尾
        if list1[j] > list1[j+1]:            #判断两个相邻数的大小，大的往后面排，小的往前面排
            list1[j],list1[j+1] = list1[j+1],list1[j]
print(list1)