from itertools import *
l = ['А', 'Н', 'Д', 'Р', 'Е', 'Й']
def f(x):
    if x[0] == 'Й': return False
    if x[-1] == 'Й': 
        return False
    if x.count('Й') > 1: 
        return False
    s = ''.join(x)
    if s.count('ЕЙ') + s.count('ЙЕ') == 0:
        return True
n = product(l, repeat=6)
fl = []
for x in n:
    if f(x)==True:
        fl.append(x)
n = len(fl)
print(n)