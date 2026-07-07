import numpy as np

# 定义系数矩阵A和常数项矩阵B
A = np.array([[2, 1], [1, -3]])
B = np.array([5, -1])

# 求解线性方程组
x = np.linalg.solve(A, B)

print("线性方程组：")
print("2x + y = 5")
print("x - 3y = -1")
print(f"\n解：x = {x[0]:.2f}, y = {x[1]:.2f}")