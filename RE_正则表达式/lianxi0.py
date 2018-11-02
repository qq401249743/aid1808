import re

f = open('/home/tarena/aid1808/RE_正则表达式/1.txt')

# pattern = r'[A-Z]\w*'

pattern = r'-?\d+\.?/?\d*%?'

l = []

for line in f:
    l += re.findall(pattern,line)

print(l)