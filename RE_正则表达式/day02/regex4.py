import re

pattern=r"(?p<dog>ab)cd(?p<pig>ef)"
regex=re.compile(pattern)

obj=regex.search("abcdefghij",pos=0,endpos=6)

print(obj.pos)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup)
print(obj.lastindex)