#VD1
from sympy import pprint, Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - 2*x*y + y**2 
pprint(bieuthuc)
#VD2
from sympy import pprint, Symbol, factor
from sympy import init_printing
init_printing(order='rev-lex')
bieu_thuc = x*x - 2*x*y + y**2
pprint(bieu_thuc)
bieu_thuc1 = factor(bieu_thuc)
pprint(bieu_thuc1)