#TH1
from sympy import Symbol
x = Symbol('x')
y = Symbol('')
bieuthuc = x**2 - 3*x + 9
giatri = bieuthuc.subs({x: 3, y: x})
print(giatri)
#TH2 
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x**2 - 3*x + 9
giatri = bieuthuc.subs({x: y, y: 3})
print(giatri) 
#TH3
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x**2 - 3*x + 9
giatri = bieuthuc.subs({y: x}).subs({x: 3})
print(giatri)
#TH4
from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x - x*y + y*y
print(bieuthuc)
bieuthuc_moi = bieuthuc.subs({x:1-y}) 
print(bieuthuc_moi)
from sympy import simplify
dongian = simplify(bieuthuc_moi)
print(dongian)
#TH5
from sympy import Symbol
from sympy import sin, cos
x = Symbol('x')
y = Symbol('y')
bt = sin(x)*cos(y) + cos(x)*sin(y)
bt_moi = simplify(bt)
print(bt_moi)