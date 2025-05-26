#VD1
from sympy import factor, Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x**3 - y**3
print(factor(bieuthuc))
#VD2
from sympy import expand, Symbol
x = Symbol('x')
y = Symbol('y')
bieu_thuc = (x-y)*(x**2 + x*y + y**2)
print(expand(bieu_thuc))