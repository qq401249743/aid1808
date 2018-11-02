import re
'''
作业:熟记正则表达式元字符
    找一个文档,使用正则表达式
    1.匹配出其中的大写字母开头的单词
    2.匹配其中所有数字 123  1.23  -1  -1.23  45%  1/2
'''
try:
    f=open('/home/tarena/aid1808/RE_正则表达式/wendan.txt')
    d=f.read()
    # pattern=r'\b[A-Z]\S*'
    pattern=r'-?\d+\.?/?\d*%?'
    l=re.findall(pattern,d)
    # l=re.findall(pattern,d)
    # print(l)
    # w=re.findall('-?\d+[./]?\d*%?',d)
    print(l)

except:
    print("打开失败")
finally:
    f.close()