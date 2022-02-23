# encoding=utf-8

import re

p = r'\d+'
text = 'AB12CD34EF'
m = re.split(p, text)
print(type(m))
print(m)
m1 = re.split(p, text, maxsplit=1)
print(type(m1))
print(m1)

m2 = re.split(p, text, maxsplit=2)
print(type(m2))
print(m2)

