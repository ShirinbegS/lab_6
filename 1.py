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
        return 1
n = product(l, repeat=6)
fl = filter(f,n)
fl = list(fl)
n = len(fl)
print(n)