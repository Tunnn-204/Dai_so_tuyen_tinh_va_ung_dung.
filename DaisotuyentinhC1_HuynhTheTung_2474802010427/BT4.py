from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')
pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5
nghiem = solve((pt1, pt2), dict=True)
print("Nghiệm của hệ phương trình là:",nghiem)
nghiem = nghiem[0]
print("Kiểm tra pt1 với nghiệm vừa tìm:", pt1.subs({x: nghiem[x], y: nghiem[y]}))
print("Kiểm tra pt2 với nghiệm vừa tìm:", pt2.subs({x: nghiem[x], y: nghiem[y]}))

