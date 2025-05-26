from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
bieuthuc = x*x -x*y - y*y
print(bieuthuc)
giatri = bieuthuc.subs({x:3, y:2})
print(giatri)
print(x)
print(y)