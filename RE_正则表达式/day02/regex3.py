import re
pattern=r"(ab)cb(?d<dog>ef)"
rexge=re.compile(pattern)
obj=rexge.search('abcbefgh')
print(obj)

#obj属性变量
print(obj.pos)
# print(obj.endpos)
# print(obj.re)    #正则表达式
# print(obj.string) #目标字符串
# print(obj.lastgroup)  #最后一组名称
# print(obj.lastindex)  #最后一组序号
# print("============")

# print(obj.span())   #匹配内容的起始位置
# print(obj.start())  #匹配内容的开始位置
# print(obj.end())    #匹配内容的结束位置

# print(obj.group())    #获取正则匹配到的内容
# print(obj.group(1))   #获取第一个子组对应内容

# print(obj.group('dog'))  #获取dog组对应内容

# print(obj.groupdict())   #捕获字典
# print(obj.groups())     #所有子组对应的内容