import re

pattern=r"(ab)cd(?p<dog>ef)"

regex=re.compile(pattern)

#获取match对象
obj=regex.search('abcdefgh',pos=0,endpos=6)
print(obj)

#obj属性变量
print(obj.pos)  #目标子串的开始位置
print(obj.endpos)#目标子串的结束位置

print(obj.re)    #正则表达式
print(obj.string) #目标字符串
print(obj.lastgroup)  #最后一组名称
print(obj.lastindex)  #最后一组序号
print("============")