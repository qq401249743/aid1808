import re

pattern=r'\d+'

s="2008 年事情多 ,08奥运,512地震"

it= re.finditer(pattern,s)

# print(dir(next(it)))
for i in it:
    #match对象group函数对象获取匹配内容
    print(i.group())

try:
    obj = re.fullmatch(r'\w+','hello 1973')
    print(obj.group())
except AttributeError as e:
    print(e)

obj=re.match(r'[A-Z]\w+','Hello world')
print(obj.group())

obj=re.search(r'\d+',s)
print(obj.group())