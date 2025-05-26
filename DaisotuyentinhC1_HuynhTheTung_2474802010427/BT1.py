from sympy import Symbol, solve
#1
x = Symbol('x')
bieuthuc = x + 3 - 5
nghiem = solve(bieuthuc)
print("Nghiệm của phương trình x + 3 - 5 = 0 là:", nghiem)
#2
bieuthuc = x**2 + 3 - 5  
nghiemx = solve(bieuthuc)
print("Nghiệm của phương trình x^2 + 3 - 5 = 0 là:", nghiemx)
print("Nghiệm thứ nhất:", nghiemx[0])
print("Nghiệm thứ hai:", nghiemx[1])
