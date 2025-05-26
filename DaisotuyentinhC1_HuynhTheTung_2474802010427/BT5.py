import numpy as np
M1 = np.array([[9, 12], [23, 30]])
print("Ma trận M1:", M1)
u = np.array([2, 1])
print("Vector u:", u)
tichM1u = M1.dot(u)
print("Kết quả M1.dot(u):", tichM1u)
tichuM1 = u.dot(M1)
print("Kết quả u.dot(M1):", tichuM1)
print("Kết quả np.dot(M1, u):", np.dot(M1, u))
print("\nKết quả np.dot(u, M1):", np.dot(u, M1))
#2 Các lệnh
mat1 = np.zeros([5,5])
print(mat1)
mat2 = np.ones( [5,5])
print(mat2)
mat3 = mat1 + 2* mat2
print(mat3)
mat4 = mat3
mat3[3][2] = 10
print(mat4)
mat5 = np.copy(mat3)
mat3[3][2] = 10
print(mat5)
mat6 = np.empty([4, 5])
print(mat6)
mat7 = np.identity(4)
print(mat7)
mat8 = np.random.random([4,5])
print(mat8)