import re

pattern=r"(\w+):(\d+)"
s="zhang:1994 li:1993"

#re直接调用
# l=re.findall(pattern,s,flags=0)
# print(l)

#通过compile对象调用
regex=re.compile(pattern,flags=0)
l=regex.findall(s,pos=0,endpos=12)
print(l)

l1=re.split(r's+',"Hello   world")
print(l1)

s=re.subn(r'\s+','##',"hello world 你好 beijing",2)
print(s)