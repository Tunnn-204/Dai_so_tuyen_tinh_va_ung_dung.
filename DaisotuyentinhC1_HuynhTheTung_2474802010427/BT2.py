from sympy import Symbol, solve
#1
x = Symbol('x')
ptb2 = x**2 + 9*x + 8
nghiem = solve(ptb2, dict=True)
print("Nghiệm của phương trình là:", nghiem)
#2
ptb2 = x**2 + x + 10
nghiemx = solve(ptb2, dict=True)
print("Nghiệm của x là:", nghiemx)
