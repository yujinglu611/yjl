import string
#文章路径
path = 'C:/Users/apple/Desktop/Walden.txt'
with open(path,'r') as text:
    #去掉文字首位的标点符号，并把首字母大写转换成小写
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    #将列表用set函数转换成集合
    words_index = set(words)
    #创建一单词为key，频率为值的字典
    counts_dict = {index:words.count(index) for index in words_index}
    #打印整理后的参数，其中利用lambda表达式，以字典中的值为排序的参数
    for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):
        print('{} -- {} times'.format(word,counts_dict[word]))