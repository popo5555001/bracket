import re
pat =r'[0-9+]+'
s="Amy was 18 year old,she likes Python and C++."
m = re.findall(pat,s)
print(m) # ['18', '++']