#VD1
from sympy import Symbol
x = Symbol('x')
f = x + x + x + 2
print(f)
#VD2
a = Symbol('Noi')
b = Symbol('Chim')
c = 3*b + 7*a
print(c)
a.name
print(a.name)
b.name 
print(b.name)
#VD3
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)
p = x*(x+2*x)
print(p)
g = (x+2)*(y+3)
print(g)
h = (x+2)*(y+3) + (x+2)*(x-3)
print(h)
j = x*(-x +2*x-x)
print(j)
k = (x+2)*(y+3)
k.expand()