import re

p = re.compile("[a-z].?")
for m in p.finditer('ab1bb2cc3de4'):
    print(m.span(), m.group())
