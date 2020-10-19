import re

zadanie = open('szyfr2.txt', 'r').read()

p = re.compile('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
print(p.findall(zadanie))


